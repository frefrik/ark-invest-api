import io
import os
import xlrd
import requests
import pandas as pd
from pathlib import Path
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from datetime import datetime, date, timedelta
from sqlalchemy.types import Integer, String, Date, Float
from requests.exceptions import ReadTimeout, ChunkedEncodingError
from .database import SessionLocal, engine
from .models import Holding, Trades, News
from .config import (
    TRADE_STATUS_URL,
    BASE_URL_HOLDINGS,
    FUND_HOLDINGS_FILES,
    FUNDS,
    HEADERS,
)

load_dotenv()


def weight_rank(df):
    df = df.sort_values(by="weight", ascending=False).reset_index(drop=True)
    df["weight_rank"] = df.index + 1

    return df


def update_trades():
    print("Checking for trades update...", end="", flush=True)
    db = SessionLocal()
    dtypes = {
        "fund": "str",
        "direction": "str",
        "ticker": "str",
        "cusip": "str",
        "company": "str",
        "shares": "int",
        "etf_percent": "float",
    }

    mapping = {
        "Date": "date",
        "FUND": "fund",
        "Direction": "direction",
        "Ticker": "ticker",
        "CUSIP": "cusip",
        "Name": "company",
        "Shares": "shares",
        "% of ETF": "etf_percent",
    }

    try:
        res = requests.get(TRADE_STATUS_URL, headers=HEADERS, timeout=10)
        html = res.text
        do_update = True
    except requests.exceptions.ReadTimeout as e:
        do_update = False
        print(e)

    if do_update:
        Path("tmp/").mkdir(exist_ok=True)

        if res.status_code == 200 and "no trades listed" not in html:
            soup = BeautifulSoup(html, "lxml")

            links = soup.find_all("a", href=True)

            for link in links:
                filename = link["href"].split("/")[-1]

                try:
                    r = requests.get(
                        link["href"], headers=HEADERS, allow_redirects=True
                    )
                    open(f"tmp/{filename}", "wb").write(r.content)

                    data = xlrd.open_workbook(
                        f"tmp/{filename}", ignore_workbook_corruption=True
                    )

                    df = pd.read_excel(
                        data, skiprows=3, parse_dates=["Date"], dtype=dtypes
                    )

                    df = df.rename(columns=mapping)
                    df["cusip"] = df["cusip"].astype("str")

                    datestr = datetime.strftime(df.iloc[0]["date"], "%Y-%m-%d")
                    fund = df.iloc[0]["fund"]

                    exists = (
                        db.query(Trades.fund, Trades.date)
                        .filter(Trades.fund == fund)
                        .filter(Trades.date == datestr)
                        .first()
                    )

                    if not exists:
                        print(
                            f"Trades - Found new data ({fund}), inserting to database"
                        )
                        df.to_sql(
                            "trades",
                            engine,
                            if_exists="append",
                            index=False,
                            dtype={
                                "date": Date,
                                "fund": String,
                                "direction": String,
                                "ticker": String,
                                "cusip": String,
                                "company": String,
                                "shares": Integer,
                                "etf_percent": Float,
                            },
                        )
                except Exception:
                    pass

    db.close()
    print("[DONE]")


def update_holdings():
    print("Checking for holdings update...", end="", flush=True)
    db = SessionLocal()
    mapping = {"market value($)": "market_value", "weight(%)": "weight"}

    for fund in FUND_HOLDINGS_FILES:
        try:
            res = requests.get(
                BASE_URL_HOLDINGS + FUND_HOLDINGS_FILES[fund], headers=HEADERS
            ).content

            df_new = pd.read_csv(io.StringIO(res.decode("utf-8")))
        except Exception:
            continue

        df_new = df_new[df_new["fund"].notna()]
        df_new["date"] = pd.to_datetime(df_new["date"])
        df_new = df_new.rename(columns=mapping)
        df_new = weight_rank(df_new)
        df_new["shares"] = df_new["shares"].astype(int)

        datestr = datetime.strftime(df_new.iloc[0]["date"], "%Y-%m-%d")

        exists = (
            db.query(Holding.fund, Holding.date)
            .filter(Holding.fund == fund)
            .filter(Holding.date == datestr)
            .first()
        )

        if not exists:
            df_new.to_sql(
                "holdings",
                engine,
                if_exists="append",
                index=False,
                dtype={
                    "date": Date,
                    "fund": String,
                    "company": String,
                    "ticker": String,
                    "cusip": String,
                    "shares": Float,
                    "market_value": Float,
                    "weight": Float,
                },
            )

    db.close()
    print("[DONE]")


def update_etf_news():
    db = SessionLocal()

    for symbol in FUNDS:
        print(f"Updating {symbol} news...", end="", flush=True)
        params = {
            "symbol": symbol,
            "from": str(date.today() - timedelta(days=1)),
            "to": str(date.today()),
            "token": os.getenv("FH_TOKEN"),
        }

        r = requests.get("https://finnhub.io/api/v1/company-news", params=params).json()

        for i in r:
            exists = (
                db.query(News.external_id).filter(News.external_id == i["id"]).first()
            )
            if not exists:
                try:
                    data = News(
                        external_id=i["id"],
                        datetime=i["datetime"],
                        category="etf",
                        related=i["related"],
                        source=i["source"],
                        headline=i["headline"],
                        summary=i["summary"],
                        url=requests.get(i["url"], headers=HEADERS, timeout=10).url,
                        image=i["image"],
                    )

                    db.add(data)
                except ReadTimeout:
                    continue
                except ChunkedEncodingError:
                    continue
                except Exception:
                    continue

        db.commit()
        print("[DONE]")

    db.close()
