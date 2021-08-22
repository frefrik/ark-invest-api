from sqlalchemy import func, desc
from sqlalchemy.orm import Session
from ..models import Fund, Holding, News, Trades


def get_etf_profile(db: Session, symbol: str):
    return db.query(Fund).filter(Fund.symbol == symbol).one()


def get_etf_holdings(db: Session, symbol: str, date_from: str, date_to: str):
    return (
        db.query(
            Holding.date,
            Holding.ticker,
            Holding.company,
            Holding.cusip,
            Holding.shares,
            Holding.market_value,
            Holding.weight,
            Holding.weight_rank,
        )
        .filter(
            Holding.fund == symbol,
            Holding.date >= date_from,
            Holding.date <= date_to,
        )
        .all()
    )


def get_etf_holdings_maxdate(db: Session, symbol: str):
    return (
        db.query(
            func.min(Holding.date).label("mindate"),
            func.max(Holding.date).label("maxdate"),
        )
        .filter(Holding.fund == symbol)
        .one()
    )


def get_etf_trades(db: Session, symbol: str, start_date: str, end_date: str):
    return (
        db.query(
            Trades.date,
            Trades.ticker,
            Trades.company,
            Trades.direction,
            Trades.cusip,
            Trades.shares,
            Trades.etf_percent,
        )
        .filter(
            Trades.fund == symbol,
            Trades.date >= start_date,
            Trades.date <= end_date,
        )
        .all()
    )


def get_etf_trades_dates(db: Session, symbol: str):
    return (
        db.query(
            func.min(Trades.date).label("mindate"),
            func.max(Trades.date).label("maxdate"),
        )
        .filter(Trades.fund == symbol)
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
    db: Session, symbol: str, direction: str, date_from: str, date_to: str
):
    if direction:
        return (
            db.query(Trades)
            .filter(
                Trades.ticker == symbol,
                Trades.direction == direction.capitalize(),
                Trades.date >= date_from,
                Trades.date <= date_to,
            )
            .order_by(Trades.date.desc(), Trades.fund)
            .all()
        )
    else:
        return (
            db.query(Trades)
            .filter(
                Trades.ticker == symbol,
                Trades.date >= date_from,
                Trades.date <= date_to,
            )
            .order_by(Trades.date.desc(), Trades.fund)
            .all()
        )


def get_stock_trades_dates(db: Session, symbol: str):
    return (
        db.query(
            func.min(Trades.date).label("mindate"),
            func.max(Trades.date).label("maxdate"),
        )
        .filter(Trades.ticker == symbol)
        .one()
    )


def get_etf_news(db: Session, symbol: str, date_from: str, date_to: str):
    if symbol:
        return (
            db.query(News)
            .filter(
                News.category == "etf",
                News.datetime >= date_from,
                News.datetime <= date_to,
                News.related == symbol,
            )
            .order_by(desc("datetime"))
            .limit(500)
            .all()
        )
    else:
        return (
            db.query(News)
            .filter(
                News.category == "etf",
                News.datetime >= date_from,
                News.datetime <= date_to,
            )
            .order_by(desc("datetime"))
            .limit(500)
            .all()
        )


def get_etf_news_min_date(db: Session, symbol: str):
    if symbol:
        return (
            db.query(
                func.min(News.datetime).label("mindate"),
            )
            .filter(News.related == symbol, News.category == "etf")
            .one()
        )[0]
    else:
        return (
            db.query(
                func.min(News.datetime).label("mindate"),
            )
            .filter(News.category == "etf")
            .one()
        )[0]
