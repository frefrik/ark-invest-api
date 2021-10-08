from datetime import date, datetime, timezone
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
    symbol: str = Query(..., description="ARK ETF symbol"),
    date_from: Optional[date] = Query(None, description="From date (ISO 8601 format)"),
    date_to: Optional[date] = Query(None, description="To date (ISO 8601 format)"),
    limit: Optional[int] = Query(None, description="Limit number of results"),
    db: Session = Depends(get_db),
):
    symbol = symbol.upper()

    data = {
        "symbol": symbol,
        "date_from": date_from,
        "date_to": date_to,
        "holdings": [],
    }

    if symbol in FUNDS:
        holding_dates = crud.get_etf_holdings_maxdate(db, symbol=symbol)

        if not date_from and not date_to:
            date_from = holding_dates.maxdate
            date_to = holding_dates.maxdate

        elif not date_to:
            date_to = holding_dates.maxdate

        elif not date_from:
            date_from = holding_dates.mindate

        if date_from > date_to:
            date_from = date_to

        holdings = crud.get_etf_holdings(
            db, symbol=symbol, date_from=date_from, date_to=date_to, limit=limit
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
    symbol: str = Query(..., description="ARK ETF symbol"),
    date_from: Optional[date] = Query(None, description="From date (ISO 8601 format)"),
    date_to: Optional[date] = Query(None, description="To date (ISO 8601 format)"),
    limit: Optional[int] = Query(None, description="Limit number of results"),
    db: Session = Depends(get_db),
):
    symbol = symbol.upper()

    data = {
        "symbol": symbol,
        "date_from": date_from,
        "date_to": date_to,
        "trades": [],
    }

    if symbol in FUNDS:
        trade_dates = crud.get_etf_trades_dates(db, symbol=symbol)

        if not date_from and not date_to:
            date_from = trade_dates.maxdate
            date_to = trade_dates.maxdate

        elif not date_to:
            date_to = trade_dates.maxdate

        elif not date_from:
            date_from = trade_dates.mindate

        trades = crud.get_etf_trades(
            db, symbol=symbol, start_date=date_from, end_date=date_to, limit=limit
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
    symbol: str = Query(..., description="ARK ETF symbol"),
    date_from: Optional[date] = Query(None, description="From date (ISO 8601 format)"),
    date_to: Optional[date] = Query(None, description="To date (ISO 8601 format)"),
    limit: Optional[int] = Query(500, description="Limit number of results"),
    db: Session = Depends(get_db),
):
    symbol = symbol.upper()

    data = {
        "symbol": symbol,
        "date_from": date_from,
        "date_to": date_to,
    }

    if symbol in FUNDS:
        min_date = crud.get_etf_news_min_date(db, symbol)

        if not date_from:
            date_from = min_date
        else:
            dt_from = datetime(
                year=date_from.year,
                month=date_from.month,
                day=date_from.day,
                hour=0,
                second=0,
            )
            date_from = int(dt_from.replace(tzinfo=timezone.utc).timestamp())

        if not date_to:
            date_to = int(datetime.now().replace(tzinfo=timezone.utc).timestamp())
        else:
            dt_to = datetime(
                year=date_to.year,
                month=date_to.month,
                day=date_to.day,
                hour=23,
                second=59,
            )
            date_to = int(dt_to.replace(tzinfo=timezone.utc).timestamp())

        news = crud.get_etf_news(
            db, symbol=symbol, date_from=date_from, date_to=date_to, limit=limit
        )

        if len(news) == 500:
            res_dates = []

            for n in news:
                res_dates.append(n.datetime)

            date_from = min(res_dates)

        data["date_from"] = date_from
        data["date_to"] = date_to
        data["news"] = news

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
    summary="Stock Profile",
)
async def stock_profile(
    symbol: str = Query(..., description="Stock symbol"),
):
    symbol = symbol.upper()

    data = {
        "symbol": symbol,
    }

    yf = YahooFinance(symbol).quote

    if not yf:
        return data

    profile = {
        "ticker": symbol,
        "name": yf.get("name"),
        "country": yf.get("country"),
        "industry": yf.get("industry"),
        "sector": yf.get("sector"),
        "fullTimeEmployees": yf.get("fullTimeEmployees"),
        "summary": yf.get("summary"),
        "website": yf.get("website"),
        "market": yf.get("market"),
        "exchange": yf.get("exchange"),
        "currency": yf.get("currency"),
        "marketCap": yf.get("marketCap"),
        "sharesOutstanding": yf.get("sharesOutstanding"),
    }

    data["profile"] = profile

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
        None, description="Filter on buy/sell", regex=r"(?i)^buy|sell$"
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
