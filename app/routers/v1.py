from datetime import datetime
from dateutil.relativedelta import relativedelta
from fastapi import APIRouter, HTTPException, Depends, Path, Query
from sqlalchemy import func, and_
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..config import FUNDS, HOLDINGS_FUND_EXAMPLE, TRADES_FUND_EXAMPLE
from ..models import Holding, Trades
from .. import schemas

v1 = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@v1.get(
    "/holdings/{fund}",
    responses={200: {"content": {"application/json": {"example": HOLDINGS_FUND_EXAMPLE}}}},
    response_model=schemas.FundHolding,
    summary="ARK fund holdings",
    tags=["Holdings"]
)
async def holdings(fund: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    fund = fund.upper()

    if fund not in FUNDS:
        raise HTTPException(
            status_code=404,
            detail="Fund must be one of: {}".format(", ".join(FUNDS)))

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
        Holding.fund == fund
    ).all()

    query_date = db.query(
        func.max(Holding.date).label('maxdate')
        ).filter(
            Holding.fund == fund
        ).one()

    data = {
        'fund': fund,
        'date': query_date[0],
        'holdings': query
    }

    return data


@v1.get(
    "/trades/{fund}",
    responses={200: {"content": {"application/json": {"example": TRADES_FUND_EXAMPLE}}}},
    response_model=schemas.FundTrades,
    tags=["Trades"],
    summary="ARK fund intraday trades")
async def trades(
    fund: str = Path(..., title="The ID of the item to get"),
    period: str = Query(
        '1d',
        regex='(?:[\s]|^)(1d|7d|1m|3m|1y|ytd)(?=[\s]|$)',
        title='woo',
        description="Valid periods: 1d, 7d, 1m, 3m, 1y, ytd"),
    db: Session = Depends(get_db)
):
    fund = fund.upper()

    if fund not in FUNDS:
        raise HTTPException(
            status_code=404,
            detail="Fund must be one of: {}".format(", ".join(FUNDS))
        )

    query_dates = db.query(
        func.min(Trades.date).label('mindate'),
        func.max(Trades.date).label('maxdate')
        ).filter(
            Trades.fund == fund
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
        Trades.fund == fund,
        Trades.date >= start_date,
        Trades.date <= end_date
    ).all()

    data = {
        'fund': fund,
        'date_from': start_date,
        'date_to': end_date,
        'trades': query
    }

    return data
