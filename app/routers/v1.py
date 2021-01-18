from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Optional
from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy import func, and_
from sqlalchemy.orm import Session
from yahooquery import Ticker
from ..database import SessionLocal
from ..models import Fund, Holding, Trades
from .. import schemas
from ..config import (
    FUNDS, FUNDS_EXAMPLE, HOLDINGS_FUND_EXAMPLE,
    TRADES_FUND_EXAMPLE, STOCK_PROFILE_EXAMPLE,
    FUND_OWNERSHIP_EXAMPLE, STOCK_TRADES_EXAMPLE
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
    responses={200: {"content": {"application/json": {"example": FUNDS_EXAMPLE}}}},
    response_model=schemas.FundProfile,
    summary="ARK Fund Profile",
    tags=["ARK ETFs"]
)
async def etf_profile(symbol: str, db: Session = Depends(get_db)):
    symbol = symbol.upper()
    if symbol not in FUNDS:
        raise HTTPException(
            status_code=404,
            detail="Fund must be one of: {}".format(", ".join(FUNDS))
        )

    query = db.query(
        Fund
    ).filter(
        Fund.symbol == symbol
    ).all()

    return {'profile': query}


@v1.get(
    "/etf/holdings",
    responses={200: {"content": {"application/json": {"example": HOLDINGS_FUND_EXAMPLE}}}},
    response_model=schemas.FundHolding,
    summary="ARK Fund Holdings",
    tags=["ARK ETFs"]
)
async def etf_holdings(symbol: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    symbol = symbol.upper()

    if symbol not in FUNDS:
        raise HTTPException(
            status_code=404,
            detail="Symbol must be one of: {}".format(", ".join(FUNDS)))

    subq = db.query(
        Holding.fund,
        func.max(Holding.date).label('maxdate')
    ).group_by(
        Holding.fund
    ).subquery('t2')

    query = db.query(
        Holding
    ).join(
        subq,
        and_(
            Holding.fund == subq.c.fund,
            Holding.date == subq.c.maxdate
        )
    ).filter(
        Holding.fund == symbol
    ).all()

    query_date = db.query(
        func.max(Holding.date).label('maxdate')
        ).filter(
            Holding.fund == symbol
        ).one()

    data = {
        'symbol': symbol,
        'date': query_date[0],
        'holdings': query
    }

    return data


@v1.get(
    "/etf/trades",
    responses={200: {"content": {"application/json": {"example": TRADES_FUND_EXAMPLE}}}},
    response_model=schemas.FundTrades,
    tags=["ARK ETFs"],
    summary="ARK Fund Trades")
async def etf_trades(
    symbol: str,
    period: str = Query(
        '1d',
        regex='(?:[\s]|^)(1d|7d|1m|3m|1y|ytd)(?=[\s]|$)',
        title='woo',
        description="Valid periods: 1d, 7d, 1m, 3m, 1y, ytd"),
    db: Session = Depends(get_db)
):
    symbol = symbol.upper()

    if symbol not in FUNDS:
        raise HTTPException(
            status_code=404,
            detail="Fund must be one of: {}".format(", ".join(FUNDS))
        )

    query_dates = db.query(
        func.min(Trades.date).label('mindate'),
        func.max(Trades.date).label('maxdate')
        ).filter(
            Trades.fund == symbol
        ).one()

    start_date = query_dates[0]
    end_date = query_dates[1]

    if period == 'ytd':
        start_date = datetime.strptime('2021-01-01', '%Y-%m-%d').date()
    elif 'y' in period:
        years = int(period.split('y')[0])
        days = years * 365
        start_date = end_date - relativedelta(years=years)
    elif 'm' in period:
        months = int(period.split('m')[0])
        start_date = end_date - relativedelta(months=months)
    elif 'd' in period:
        days = int(period.split('d')[0])
        start_date = end_date - relativedelta(days=(days - 1))

    query = db.query(
        Trades
    ).filter(
        Trades.fund == symbol,
        Trades.date >= start_date,
        Trades.date <= end_date
    ).all()

    data = {
        'symbol': symbol,
        'date_from': start_date,
        'date_to': end_date,
        'trades': query
    }

    return data


@v1.get(
    "/stock/profile",
    responses={200: {"content": {"application/json": {"example": STOCK_PROFILE_EXAMPLE}}}},
    response_model=schemas.StockProfile,
    summary="Stock Profile",
    tags=["Stock"]
)
async def stock_profile(symbol: str):
    symbol = symbol.upper()

    yf = Ticker(symbol)
    quotes = yf.quotes
    asset_profile = yf.asset_profile

    if 'No data found' in quotes:
        raise HTTPException(
                    status_code=404,
                    detail=f"Ticker {symbol} not found."
                )

    quotes = quotes[symbol]
    asset_profile = asset_profile[symbol]

    data = {
        'ticker': symbol,
        'name': quotes.get('longName'),
        'country': asset_profile.get('country'),
        'industry': asset_profile.get('industry'),
        'sector': asset_profile.get('sector'),
        'fullTimeEmployees': asset_profile.get('fullTimeEmployees'),
        'summary': asset_profile.get('longBusinessSummary'),
        'website': asset_profile.get('website'),
        'market': quotes.get('market'),
        'exchange': quotes.get('fullExchangeName'),
        'currency': quotes.get('currency'),
        'marketCap': quotes.get('marketCap'),
        'sharesOutstanding': quotes.get('sharesOutstanding')
    }

    return data


@v1.get(
    "/stock/fund-ownership",
    responses={200: {"content": {"application/json": {"example": FUND_OWNERSHIP_EXAMPLE}}}},
    response_model=schemas.FundOwnership,
    summary="ARK Fund Ownership",
    tags=["Stock"]
)
async def stock_fundownership(symbol: str, db: Session = Depends(get_db)):
    symbol = symbol.upper()

    subq = db.query(
        Holding.fund,
        func.max(Holding.date).label('maxdate')
    ).group_by(
        Holding.fund
    ).subquery('t2')

    query = db.query(
        Holding
    ).join(
        subq,
        and_(
            Holding.date == subq.c.maxdate
        )
    ).filter(
        Holding.ticker == symbol
    ).all()

    query_date = db.query(
        func.max(Holding.date).label('maxdate')
        ).filter(
            Holding.ticker == symbol
        ).first()

    totals = {
        'funds': len([r.fund for r in query]),
        'shares': sum([r.shares for r in query]),
        'market_value': sum([r.market_value for r in query])
    }

    data = {
        'symbol': symbol,
        'date': query_date[0],
        'ownership': query,
        'totals': totals
    }

    return data


@v1.get(
    "/stock/trades",
    responses={200: {"content": {"application/json": {"example": STOCK_TRADES_EXAMPLE}}}},
    response_model=schemas.StockTrades,
    summary="ARK Stock Trades",
    tags=["Stock"]
)
async def stock_trades(symbol: str, direction: Optional[str] = Query(None, regex="^buy|sell$"), db: Session = Depends(get_db)):
    symbol = symbol.upper()

    if direction:
        tradelist = db.query(
            Trades
        ).filter(
            Trades.ticker == symbol,
            Trades.direction == direction.capitalize()
        ).order_by(
            Trades.date.desc(),
            Trades.fund
        ).all()
    else:
        tradelist = db.query(
            Trades
        ).filter(
            Trades.ticker == symbol
        ).order_by(
            Trades.date.desc(),
            Trades.fund
        ).all()

    if not tradelist:
        raise HTTPException(
                    status_code=404,
                    detail=f"No ARK trades found for {symbol}"
                )

    query_dates = db.query(
        func.min(Trades.date).label('mindate'),
        func.max(Trades.date).label('maxdate')
        ).filter(
            Trades.ticker == symbol
        ).one()

    start_date = query_dates[0]
    end_date = query_dates[1]

    data = {
        'symbol': symbol,
        'date_from': start_date,
        'date_to': end_date,
        'trades': tradelist
    }

    return data
