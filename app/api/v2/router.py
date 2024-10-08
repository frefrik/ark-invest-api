import re
from datetime import date, datetime, UTC
from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.config import FUNDS, RESPONSES
from app.database import SessionLocal
from app.src.yahoofinance import YahooFinance

from . import crud, schemas

v2 = APIRouter(tags=["v2"])


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def validate_symbols(symbols):
    symbols = re.findall(r"[\w\-.=^&]+", symbols.upper())

    valid_symbols = []

    for symbol in symbols:
        if symbol in FUNDS:
            valid_symbols.append(symbol)

    return valid_symbols


@v2.get(
    "/etf/profile",
    responses={
        200: {
            "content": {"application/json": {"example": RESPONSES["v2"]["etf_profile"]}}
        }
    },
    response_model=schemas.V2_FundProfile,
    summary="ETF Profile",
)
async def etf_profile(
    symbol: str = Query(..., description="ARK ETF symbol"),
    db: Session = Depends(get_db),
):
    symbol = symbol.upper()

    data = {
        "symbol": symbol,
    }

    if symbol in FUNDS:
        profile = crud.get_etf_profile(db, symbol=symbol)
        data["profile"] = profile

    return data


@v2.get(
    "/etf/holdings",
    responses={
        200: {
            "content": {
                "application/json": {"example": RESPONSES["v2"]["etf_holdings"]}
            }
        }
    },
    response_model=schemas.V2_FundHolding,
    summary="ETF Holdings",
)
async def etf_holdings(
    symbol: str = Query(..., description="ARK ETF symbols"),
    date_from: Optional[date] = Query(None, description="From date (ISO 8601 format)"),
    date_to: Optional[date] = Query(None, description="To date (ISO 8601 format)"),
    limit: Optional[int] = Query(None, description="Limit number of results"),
    db: Session = Depends(get_db),
):
    symbols = validate_symbols(symbol)

    data = {
        "symbol": ",".join(map(str, symbols)),
        "date_from": date_from,
        "date_to": date_to,
        "holdings": [],
    }

    if symbols:
        holdings = None
        holding_dates = crud.get_etf_holdings_dates(db, symbols=symbols)
        min_date = min(holding_dates)[0]
        max_date = max(holding_dates)[0]

        if not date_from and not date_to:
            date_from = min_date
            date_to = max_date

            holdings = crud.get_etf_current_holdings(db, symbols=symbols, limit=limit)

        elif not date_to:
            date_to = max_date

        elif not date_from:
            date_from = min_date

        if date_from > date_to:
            date_from = date_to

        if not holdings:
            holdings = crud.get_etf_holdings(
                db, symbols=symbols, date_from=date_from, date_to=date_to, limit=limit
            )

        data["date_from"] = date_from
        data["date_to"] = date_to
        data["holdings"] = holdings

    return data


@v2.get(
    "/etf/trades",
    responses={
        200: {
            "content": {"application/json": {"example": RESPONSES["v2"]["etf_trades"]}}
        }
    },
    response_model=schemas.V2_FundTrades,
    summary="ETF Trades",
)
async def etf_trades(
    symbol: str = Query(..., description="ARK ETF symbols"),
    date_from: Optional[date] = Query(None, description="From date (ISO 8601 format)"),
    date_to: Optional[date] = Query(None, description="To date (ISO 8601 format)"),
    limit: Optional[int] = Query(None, description="Limit number of results"),
    db: Session = Depends(get_db),
):
    symbols = validate_symbols(symbol)

    data = {
        "symbol": ",".join(map(str, symbols)),
        "date_from": date_from,
        "date_to": date_to,
        "trades": [],
    }

    if symbols:
        trade_dates = crud.get_etf_trades_dates(db, symbols=symbols)

        if not date_from and not date_to:
            date_from = trade_dates.maxdate
            date_to = trade_dates.maxdate

        elif not date_to:
            date_to = trade_dates.maxdate

        elif not date_from:
            date_from = trade_dates.mindate

        trades = crud.get_etf_trades(
            db, symbols=symbols, start_date=date_from, end_date=date_to, limit=limit
        )

        data["date_from"] = date_from
        data["date_to"] = date_to
        data["trades"] = trades

    return data


@v2.get(
    "/etf/news",
    responses={
        200: {"content": {"application/json": {"example": RESPONSES["v2"]["etf_news"]}}}
    },
    response_model=schemas.V2_FundNews,
    summary="ETF News",
)
async def etf_news(
    symbol: str = Query(..., description="ARK ETF symbols"),
    date_from: Optional[date] = Query(None, description="From date (ISO 8601 format)"),
    date_to: Optional[date] = Query(None, description="To date (ISO 8601 format)"),
    limit: Optional[int] = Query(500, description="Limit number of results"),
    db: Session = Depends(get_db),
):
    symbols = validate_symbols(symbol)

    data = {
        "symbol": ",".join(map(str, symbols)),
        "date_from": date_from,
        "date_to": date_to,
    }

    if symbols:
        min_date = crud.get_etf_news_min_date(db, symbols)

        if not date_from:
            date_from = min_date
        else:
            date_from = date(
                year=date_from.year,
                month=date_from.month,
                day=date_from.day,
            )

        if not date_to:
            date_to = datetime.now(UTC).date()
        else:
            date_to = date(
                year=date_to.year,
                month=date_to.month,
                day=date_to.day,
            )

        news = crud.get_etf_news(
            db, symbols=symbols, date_from=date_from, date_to=date_to, limit=limit
        )

        if len(news) == 500:
            res_dates = []

            for n in news:
                res_dates.append(datetime.fromtimestamp(n.datetime).date())

            date_from = min(res_dates)

        data["date_from"] = date_from
        data["date_to"] = date_to
        data["news"] = news

    return data


@v2.get(
    "/etf/performance",
    responses={
        200: {
            "content": {
                "application/json": {"example": RESPONSES["v2"]["etf_performance"]}
            }
        }
    },
    response_model=schemas.V2_FundPerformance,
    summary="ETF Performance",
)
async def etf_performance(
    symbol: str = Query(..., description="ARK ETF symbol"),
    formatted: bool = Query(False, description="Return formatted values"),
):
    symbol = symbol.upper()
    symbols = validate_symbols(symbol)

    data = {
        "symbol": ",".join(map(str, symbols)),
        "performance": [],
    }

    for s in symbols:
        yf = YahooFinance(s, formatted=True)
        yf_perf = yf.fund_performance

        if not yf_perf:
            return data

        value = "fmt" if formatted else "raw"
        overview = yf_perf["performanceOverview"]
        trailing = yf_perf["trailingReturns"]
        annual = yf_perf["annualTotalReturns"]["returns"]

        annual_returns = []
        for i in annual:
            annual_returns.append(
                {
                    "year": i["year"],
                    "value": i.get("annualValue", {}).get(value),
                }
            )

        performance = {
            "fund": s,
            "overview": {
                "asOfDate": overview.get("asOfDate", {}).get("fmt"),
                "ytdReturn": overview.get("ytdReturnPct", {}).get(value),
                "oneYearReturn": overview.get("oneYearTotalReturn", {}).get(value),
                "threeYearReturn": overview.get("threeYearTotalReturn", {}).get(value),
            },
            "trailingReturns": {
                "asOfDate": trailing.get("asOfDate", {}).get("fmt"),
                "ytd": trailing.get("ytd", {}).get(value),
                "oneMonth": trailing.get("oneMonth", {}).get(value),
                "threeMonth": trailing.get("threeMonth", {}).get(value),
                "oneYear": trailing.get("oneYear", {}).get(value),
                "threeYear": trailing.get("threeYear", {}).get(value),
                "fiveYear": trailing.get("fiveYear", {}).get(value),
                "tenYear": trailing.get("tenYear", {}).get(value),
            },
            "annualReturns": annual_returns,
        }

        data["performance"].append(performance)

    return data


@v2.get(
    "/stock/profile",
    responses={
        200: {
            "content": {
                "application/json": {"example": RESPONSES["v2"]["stock_profile"]}
            }
        }
    },
    response_model=schemas.V2_StockProfile,
    response_model_exclude_none=True,
    summary="Stock Profile",
)
async def stock_profile(
    symbol: str = Query(..., description="Stock symbol"),
    price: bool = Query(False, description="Show current share price"),
):
    symbol = symbol.upper()

    data = {
        "symbol": symbol,
    }

    yf_quote = YahooFinance(symbol).quote

    if not yf_quote:
        return data

    profile = {
        "ticker": symbol,
        "name": yf_quote.get("name"),
        "country": yf_quote.get("country"),
        "industry": yf_quote.get("industry"),
        "sector": yf_quote.get("sector"),
        "fullTimeEmployees": yf_quote.get("fullTimeEmployees"),
        "summary": yf_quote.get("summary"),
        "website": yf_quote.get("website"),
        "market": yf_quote.get("market"),
        "exchange": yf_quote.get("exchange"),
        "currency": yf_quote.get("currency"),
        "marketCap": yf_quote.get("marketCap"),
        "sharesOutstanding": yf_quote.get("sharesOutstanding"),
        "price": None,
        "change": None,
        "changep": None,
        "last_trade": None,
    }

    data["profile"] = profile

    if price:
        yf_price = YahooFinance(symbol).price
        profile["price"] = yf_price.get("price")
        profile["change"] = yf_price.get("change")
        profile["changep"] = yf_price.get("changep")
        profile["last_trade"] = yf_price.get("last_trade")

    return data


@v2.get(
    "/stock/fund-ownership",
    responses={
        200: {
            "content": {
                "application/json": {"example": RESPONSES["v2"]["stock_fund_ownership"]}
            }
        }
    },
    response_model=schemas.V2_FundOwnership,
    summary="Stock Fund Ownership",
)
async def stock_fundownership(
    symbol: str = Query(..., description="Stock symbol"),
    date_from: Optional[date] = Query(None, description="From date (ISO 8601 format)"),
    date_to: Optional[date] = Query(None, description="To date (ISO 8601 format)"),
    limit: Optional[int] = Query(None, description="Limit number of results"),
    db: Session = Depends(get_db),
):
    limit_count = 0
    symbol = symbol.upper()

    data = {
        "symbol": symbol,
        "data": [],
    }

    ownership_dates = crud.get_stock_fundownership_dates(db, symbol=symbol)

    if None in ownership_dates:
        return data

    if not date_from and not date_to:
        date_from = ownership_dates.maxdate
        date_to = ownership_dates.maxdate

    elif not date_to:
        date_to = ownership_dates.maxdate

    elif not date_from:
        date_from = ownership_dates.mindate

    distinct_dates = crud.get_stock_fundownership_distinct_dates(
        db, symbol=symbol, date_from=date_from, date_to=date_to
    )

    for d in distinct_dates:
        limit_count += 1
        o_date = d[0]
        ownership = crud.get_stock_fundownership(db, symbol=symbol, date=o_date)

        totals = {
            "funds": len([r.fund for r in ownership]),
            "shares": sum([r.shares for r in ownership]),
            "market_value": sum([r.market_value for r in ownership]),
        }

        data["data"].append(
            {
                "date": o_date,
                "ownership": ownership,
                "totals": totals,
            }
        )

        if limit and limit_count == limit:
            break

    data["date_from"] = date_from
    data["date_to"] = date_to

    return data


@v2.get(
    "/stock/trades",
    responses={
        200: {
            "content": {
                "application/json": {"example": RESPONSES["v2"]["stock_trades"]}
            }
        }
    },
    response_model=schemas.V2_StockTrades,
    summary="Stock Trades",
)
async def stock_trades(
    symbol: str = Query(..., description="Stock symbol"),
    date_from: Optional[date] = Query(None, description="From date (ISO 8601 format)"),
    date_to: Optional[date] = Query(None, description="To date (ISO 8601 format)"),
    limit: Optional[int] = Query(None, description="Limit number of results"),
    direction: Optional[str] = Query(
        None, description="Filter on buy/sell", pattern=r"(?i)^buy|sell$"
    ),
    db: Session = Depends(get_db),
):
    symbol = symbol.upper()

    data = {
        "symbol": symbol,
    }

    trade_dates = crud.get_stock_trades_dates(db, symbol=symbol)

    if not None in trade_dates:
        if not date_from:
            date_from = trade_dates.mindate
        if not date_to:
            date_to = trade_dates.maxdate

        trades = crud.get_stock_trades(
            db,
            symbol=symbol,
            direction=direction,
            date_from=date_from,
            date_to=date_to,
            limit=limit,
        )

        data["trades"] = trades

    data["date_from"] = date_from
    data["date_to"] = date_to

    return data


@v2.get(
    "/stock/price",
    responses={
        200: {
            "content": {"application/json": {"example": RESPONSES["v2"]["stock_price"]}}
        }
    },
    response_model=schemas.V2_StockPrice,
    summary="Stock Price",
)
async def stock_price(
    symbol: str = Query(..., description="Stock symbol"),
):
    symbol = symbol.upper()

    data = {
        "symbol": symbol,
    }

    price = YahooFinance(symbol).price

    if not price:
        return data

    data.update(price)

    return data
