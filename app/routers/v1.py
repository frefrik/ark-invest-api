from datetime import datetime, date, timezone
from dateutil.relativedelta import relativedelta
from typing import Optional
from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from yahooquery import Ticker
from ..database import SessionLocal
from .. import schemas, crud
from ..config import (
    FUNDS,
    ETF_PROFILE_EXAMPLE,
    ETF_HOLDINGS_EXAMPLE,
    ETF_TRADES_EXAMPLE,
    ETF_NEWS_EXAMPLE,
    STOCK_PROFILE_EXAMPLE,
    STOCK_FUND_OWNERSHIP_EXAMPLE,
    STOCK_TRADES_EXAMPLE,
)

v1 = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@v1.get(
    "/etf/profile",
    responses={
        200: {"content": {"application/json": {"example": ETF_PROFILE_EXAMPLE}}}
    },
    response_model=schemas.FundProfile,
    summary="ETF Profile",
    tags=["ARK ETFs"],
)
async def etf_profile(
    symbol: Optional[str] = Query(None, regex=r"^\S+$"),
    db: Session = Depends(get_db),
):
    if symbol:
        symbol = symbol.upper()
        if symbol not in FUNDS:
            raise HTTPException(
                status_code=404,
                detail="symbol must be one of: {}".format(", ".join(FUNDS)),
            )

    profile = crud.get_etf_profile(db, symbol=symbol)

    return {"profile": profile}


@v1.get(
    "/etf/holdings",
    responses={
        200: {"content": {"application/json": {"example": ETF_HOLDINGS_EXAMPLE}}}
    },
    response_model=schemas.FundHolding,
    summary="ETF Holdings",
    tags=["ARK ETFs"],
)
async def etf_holdings(
    symbol: str = Query(..., regex=r"^\S+$"),
    holding_date: Optional[date] = Query(
        None,
        description="Fund holding date in ISO 8601 format",
        alias="date",
    ),
    db: Session = Depends(get_db),
):
    symbol = symbol.upper()

    if symbol not in FUNDS:
        raise HTTPException(
            status_code=404, detail="symbol must be one of: {}".format(", ".join(FUNDS))
        )

    maxdate = crud.get_etf_holdings_maxdate(db, symbol=symbol)

    if not holding_date:
        holding_date = maxdate.date

    holdings = crud.get_etf_holdings(db, symbol=symbol, holding_date=holding_date)

    data = {"symbol": symbol, "date": holding_date, "holdings": holdings}

    return data


@v1.get(
    "/etf/trades",
    responses={200: {"content": {"application/json": {"example": ETF_TRADES_EXAMPLE}}}},
    response_model=schemas.FundTrades,
    tags=["ARK ETFs"],
    summary="ETF Trades",
)
async def etf_trades(
    symbol: str = Query(..., regex=r"^\S+$"),
    period: str = Query(
        "1d",
        regex=r"(?:[\s]|^)(1d|7d|1m|3m|1y|ytd)(?=[\s]|$)",
        description="Valid periods: 1d, 7d, 1m, 3m, 1y, ytd",
    ),
    db: Session = Depends(get_db),
):
    symbol = symbol.upper()

    if symbol not in FUNDS:
        raise HTTPException(
            status_code=404, detail="symbol must be one of: {}".format(", ".join(FUNDS))
        )

    dates = crud.get_etf_trades_dates(db, symbol=symbol)

    start_date = dates[0]
    end_date = dates[1]

    if not end_date:
        end_date = crud.get_etf_trades_maxdate(db)

    if period == "ytd":
        start_date = datetime.strptime("2021-01-01", "%Y-%m-%d").date()
    elif "y" in period:
        years = int(period.split("y")[0])
        days = years * 365
        start_date = end_date - relativedelta(years=years)
    elif "m" in period:
        months = int(period.split("m")[0])
        start_date = end_date - relativedelta(months=months)
    elif "d" in period:
        days = int(period.split("d")[0])
        start_date = end_date - relativedelta(days=(days - 1))

    trades = crud.get_etf_trades(
        db, symbol=symbol, start_date=start_date, end_date=end_date
    )

    data = {
        "symbol": symbol,
        "date_from": start_date,
        "date_to": end_date,
        "trades": trades,
    }

    return data


@v1.get(
    "/etf/news",
    responses={200: {"content": {"application/json": {"example": ETF_NEWS_EXAMPLE}}}},
    response_model=schemas.FundNews,
    summary="ETF News",
    tags=["ARK ETFs"],
)
async def etf_news(
    symbol: Optional[str] = Query(None, regex=r"^\S+$"),
    date_from: Optional[date] = Query(None),
    date_to: Optional[date] = Query(None),
    db: Session = Depends(get_db),
):
    if symbol:
        symbol = symbol.upper()
        if symbol not in FUNDS:
            raise HTTPException(
                status_code=404,
                detail="symbol must be one of: {}".format(", ".join(FUNDS)),
            )

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
            year=date_to.year, month=date_to.month, day=date_to.day, hour=23, second=59
        )
        date_to = int(dt_to.replace(tzinfo=timezone.utc).timestamp())

    news = crud.get_etf_news(db, symbol=symbol, date_from=date_from, date_to=date_to)

    if len(news) == 500:
        res_dates = []

        for n in news:
            res_dates.append(n.datetime)

        date_from = min(res_dates)

    data = {
        "symbol": symbol,
        "date_from": date_from,
        "date_to": date_to,
        "news": news,
    }

    return data


@v1.get(
    "/stock/profile",
    responses={
        200: {"content": {"application/json": {"example": STOCK_PROFILE_EXAMPLE}}}
    },
    response_model=schemas.StockProfile,
    summary="Stock Profile",
    tags=["Stock"],
)
async def stock_profile(symbol: str = Query(..., regex=r"^\S+$")):
    symbol = symbol.upper()

    yf = Ticker(symbol)
    quotes = yf.quotes
    asset_profile = yf.asset_profile

    if (
        "No fundamentals data found" in asset_profile[symbol]
        or "Quote not found" in asset_profile[symbol]
    ):
        raise HTTPException(status_code=404, detail=f"symbol {symbol} not found.")

    quotes = quotes[symbol]
    asset_profile = asset_profile[symbol]

    data = {
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

    return data


@v1.get(
    "/stock/fund-ownership",
    responses={
        200: {
            "content": {"application/json": {"example": STOCK_FUND_OWNERSHIP_EXAMPLE}}
        }
    },
    response_model=schemas.FundOwnership,
    summary="Stock Fund Ownership",
    tags=["Stock"],
)
async def stock_fundownership(
    symbol: str = Query(..., regex=r"^\S+$"), db: Session = Depends(get_db)
):
    symbol = symbol.upper()

    ownership = crud.get_stock_fundownership(db, symbol=symbol)
    maxdate = crud.get_stock_fundownership_maxdate(db, symbol=symbol)

    totals = {
        "funds": len([r.fund for r in ownership]),
        "shares": sum([r.shares for r in ownership]),
        "market_value": sum([r.market_value for r in ownership]),
    }

    data = {
        "symbol": symbol,
        "date": maxdate,
        "ownership": ownership,
        "totals": totals,
    }

    return data


@v1.get(
    "/stock/trades",
    responses={
        200: {"content": {"application/json": {"example": STOCK_TRADES_EXAMPLE}}}
    },
    response_model=schemas.StockTrades,
    summary="Stock Trades",
    tags=["Stock"],
)
async def stock_trades(
    symbol: str = Query(..., regex=r"^\S+$"),
    direction: Optional[str] = Query(None, regex=r"^buy|sell$"),
    date_from: Optional[date] = Query(None),
    date_to: Optional[date] = Query(None),
    db: Session = Depends(get_db),
):
    symbol = symbol.upper()

    dates = crud.get_stock_trades_dates(db, symbol=symbol)

    if None in dates:
        raise HTTPException(status_code=404, detail=f"No ARK trades found for {symbol}")

    if not date_from:
        date_from = dates[0]
    if not date_to:
        date_to = dates[1]

    trades = crud.get_stock_trades(
        db, symbol=symbol, direction=direction, date_from=date_from, date_to=date_to
    )

    data = {
        "symbol": symbol,
        "date_from": date_from,
        "date_to": date_to,
        "trades": trades,
    }

    return data
