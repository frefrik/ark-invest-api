from datetime import date, datetime, timezone, UTC

from sqlalchemy import desc, func
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_

from app.models import Fund, Holding, News, Trades


def get_etf_profile(db: Session, symbol: str):
    return db.query(Fund).filter(Fund.symbol == symbol).one()


def get_etf_current_holdings(db: Session, symbols: str, limit: int):
    subq = (
        db.query(
            Holding.fund,
            func.max(Holding.date).label("maxdate"),
        )
        .filter(
            Holding.fund.in_([s for s in symbols]),
        )
        .group_by(Holding.fund)
        .subquery()
    )

    q = (
        db.query(
            Holding.fund,
            Holding.date,
            Holding.ticker,
            Holding.company,
            Holding.cusip,
            Holding.shares,
            Holding.market_value,
            Holding.share_price,
            Holding.weight,
            Holding.weight_rank,
        )
        .join(
            subq,
            and_(
                Holding.fund == subq.c.fund,
                Holding.date == subq.c.maxdate,
            ),
        )
        .order_by(
            Holding.date,
            Holding.fund,
            Holding.weight_rank,
        )
    )

    if limit:
        return q.order_by("date", "weight_rank").limit(limit).all()
    else:
        return q.all()


def get_etf_holdings(
    db: Session, symbols: str, date_from: str, date_to: str, limit: int
):
    q = (
        db.query(
            Holding.fund,
            Holding.date,
            Holding.ticker,
            Holding.company,
            Holding.cusip,
            Holding.shares,
            Holding.market_value,
            Holding.share_price,
            Holding.weight,
            Holding.weight_rank,
        )
        .filter(
            Holding.fund.in_([s for s in symbols]),
            Holding.date >= date_from,
            Holding.date <= date_to,
        )
        .order_by(
            Holding.date,
            Holding.fund,
            Holding.weight_rank,
        )
    )

    if limit:
        return q.order_by("date", "weight_rank").limit(limit).all()
    else:
        return q.all()


def get_etf_holdings_dates(db: Session, symbols: str):
    return (
        db.query(
            func.max(Holding.date).label("maxdate"),
        )
        .filter(Holding.fund.in_([s for s in symbols]))
        .group_by(Holding.fund)
        .all()
    )


def get_etf_trades(
    db: Session, symbols: str, start_date: str, end_date: str, limit: int
):
    if not start_date:
        start_date = datetime.now().date()
    if not end_date:
        end_date = datetime.now().date()

    q = (
        db.query(
            Trades.fund,
            Trades.date,
            Trades.ticker,
            Trades.company,
            Trades.direction,
            Trades.cusip,
            Trades.shares,
            Trades.etf_percent,
        )
        .filter(
            Trades.fund.in_([s for s in symbols]),
            Trades.date >= start_date,
            Trades.date <= end_date,
        )
        .order_by(
            Trades.date,
            Trades.fund,
            Trades.etf_percent.desc(),
        )
    )

    if limit:
        return q.limit(limit).all()
    else:
        return q.all()


def get_etf_trades_dates(db: Session, symbols: str):
    return (
        db.query(
            func.min(Trades.date).label("mindate"),
            func.max(Trades.date).label("maxdate"),
        )
        .filter(Trades.fund.in_([s for s in symbols]))
        .one()
    )


def get_etf_trades_maxdate(db: Session):
    return (
        db.query(
            func.max(Trades.date).label("maxdate"),
        ).one()
    )[0]


def get_stock_fundownership_distinct_dates(
    db: Session, symbol: str, date_from: str, date_to: str
):
    return (
        db.query(Holding.date)
        .filter(
            Holding.ticker == symbol,
            Holding.date >= date_from,
            Holding.date <= date_to,
        )
        .distinct()
    )


def get_stock_fundownership(db: Session, symbol: str, date: str):
    return (
        db.query(Holding)
        .filter(
            Holding.ticker == symbol,
            Holding.date == date,
        )
        .all()
    )


def get_stock_fundownership_dates(db: Session, symbol: str):
    return (
        db.query(
            func.min(Holding.date).label("mindate"),
            func.max(Holding.date).label("maxdate"),
        )
        .filter(Holding.ticker == symbol)
        .first()
    )


def get_stock_trades(
    db: Session, symbol: str, direction: str, date_from: str, date_to: str, limit: int
):
    if direction:
        q = (
            db.query(Trades)
            .filter(
                Trades.ticker == symbol,
                Trades.direction == direction.capitalize(),
                Trades.date >= date_from,
                Trades.date <= date_to,
            )
            .order_by(Trades.date.desc(), Trades.fund)
        )

    else:
        q = (
            db.query(Trades)
            .filter(
                Trades.ticker == symbol,
                Trades.date >= date_from,
                Trades.date <= date_to,
            )
            .order_by(Trades.date.desc(), Trades.fund)
        )

    if limit:
        return q.limit(limit).all()
    else:
        return q.all()


def get_stock_trades_dates(db: Session, symbol: str):
    return (
        db.query(
            func.min(Trades.date).label("mindate"),
            func.max(Trades.date).label("maxdate"),
        )
        .filter(Trades.ticker == symbol)
        .one()
    )


def get_etf_news(db: Session, symbols: str, date_from: date, date_to: date, limit: int):
    epoch_date_from = int(datetime(date_from.year, date_from.month, date_from.day, tzinfo=timezone.utc).timestamp())
    epoch_date_to = int(datetime(date_to.year, date_to.month, date_to.day, 23, 59, 59, tzinfo=timezone.utc).timestamp())

    return (
        db.query(News)
        .filter(
            News.category == "etf",
            News.datetime >= epoch_date_from,
            News.datetime <= epoch_date_to,
            News.related.in_([s for s in symbols]),
        )
        .order_by(desc("datetime"))
        .limit(limit)
        .all()
    )


def get_etf_news_min_date(db: Session, symbols: str):
    epoch_min_date = (
        db.query(
            func.min(News.datetime).label("mindate"),
        )
        .filter(
            News.related.in_([s for s in symbols]),
            News.category == "etf",
        )
        .one()
    )[0]

    if not epoch_min_date:
        return datetime.now(UTC).date()

    return datetime.fromtimestamp(epoch_min_date).date()
