from datetime import datetime, date, timezone
from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from yahooquery import Ticker
from app.database import SessionLocal
from . import crud
from . import schemas
from app.config import (
    FUNDS,
    ETF_PROFILE_EXAMPLE,
    ETF_HOLDINGS_EXAMPLE,
    ETF_TRADES_EXAMPLE,
    ETF_NEWS_EXAMPLE,
    STOCK_PROFILE_EXAMPLE,
    STOCK_FUND_OWNERSHIP_EXAMPLE,
    STOCK_TRADES_EXAMPLE,
)

v2 = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@v2.get(
    "/etf/profile",
    responses={
        200: {"content": {"application/json": {"example": ETF_PROFILE_EXAMPLE}}}
    },
    response_model=schemas.FundProfile,
    summary="ETF Profile",
    tags=["v2"],
)
async def etf_profile(
    symbol: str = Query("", regex=r"^\S+$"),
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
        200: {"content": {"application/json": {"example": ETF_HOLDINGS_EXAMPLE}}}
    },
    response_model=schemas.FundHolding,
    summary="ETF Holdings",
    tags=["v2"],
)
async def etf_holdings(
    symbol: str = Query("", regex=r"^\S+$"),
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    limit: Optional[int] = None,
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
    responses={200: {"content": {"application/json": {"example": ETF_TRADES_EXAMPLE}}}},
    response_model=schemas.FundTrades,
    tags=["v2"],
    summary="ETF Trades",
)
async def etf_trades(
    symbol: str = Query("", regex=r"^\S+$"),
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    limit: Optional[int] = None,
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
    responses={200: {"content": {"application/json": {"example": ETF_NEWS_EXAMPLE}}}},
    response_model=schemas.FundNews,
    summary="ETF News",
    tags=["v2"],
)
async def etf_news(
    symbol: str = Query("", regex=r"^\S+$"),
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    limit: Optional[int] = 500,
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
        200: {"content": {"application/json": {"example": STOCK_PROFILE_EXAMPLE}}}
    },
    response_model=schemas.StockProfile,
    summary="Stock Profile",
    tags=["v2"],
)
async def stock_profile(
    symbol: str = Query("", regex=r"^\S+$"),
):
    symbol = symbol.upper()

    yf = Ticker(symbol)
    quotes = yf.quotes
    asset_profile = yf.asset_profile

    data = {
        "symbol": symbol,
    }

    if (
        "No fundamentals data found" in asset_profile[symbol]
        or "Quote not found" in asset_profile[symbol]
    ):
        return data

    quotes = quotes[symbol]
    asset_profile = asset_profile[symbol]

    profile = {
        "ticker": symbol,
        "name": quotes.get("longName"),
        "country": asset_profile.get("country"),
        "industry": asset_profile.get("industry"),
        "sector": asset_profile.get("sector"),
        "fullTimeEmployees": asset_profile.get("fullTimeEmployees"),
        "summary": asset_profile.get("longBusinessSummary"),
        "website": asset_profile.get("website"),
        "market": quotes.get("market"),
        "exchange": quotes.get("fullExchangeName"),
        "currency": quotes.get("currency"),
        "marketCap": quotes.get("marketCap"),
        "sharesOutstanding": quotes.get("sharesOutstanding"),
    }

    data["profile"] = profile

    return data


@v2.get(
    "/stock/fund-ownership",
    responses={
        200: {
            "content": {"application/json": {"example": STOCK_FUND_OWNERSHIP_EXAMPLE}}
        }
    },
    response_model=schemas.FundOwnership,
    summary="Stock Fund Ownership",
    tags=["v2"],
)
async def stock_fundownership(
    symbol: str = Query("", regex=r"^\S+$"),
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    limit: Optional[int] = None,
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
        200: {"content": {"application/json": {"example": STOCK_TRADES_EXAMPLE}}}
    },
    response_model=schemas.StockTrades,
    summary="Stock Trades",
    tags=["v2"],
)
async def stock_trades(
    symbol: str = Query("", regex=r"^\S+$"),
    direction: Optional[str] = Query(None, regex=r"(?i)^buy|sell$"),
    date_from: Optional[date] = None,
    date_to: Optional[date] = None,
    limit: Optional[int] = None,
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
