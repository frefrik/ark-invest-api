from sqlalchemy import func, and_, desc
from sqlalchemy.orm import Session
from .models import Fund, Holding, News, Trades


def get_etf_profile(db: Session, symbol: str):
    if symbol:
        return db.query(Fund).filter(Fund.symbol == symbol).all()
    else:
        return db.query(Fund).order_by(Fund.symbol).all()


def get_etf_holdings(db: Session, symbol: str, holding_date: str):
    return (
        db.query(Holding)
        .filter(Holding.fund == symbol, Holding.date == holding_date)
        .all()
    )


def get_etf_holdings_maxdate(db: Session, symbol: str):
    return (
        db.query(func.max(Holding.date).label("date"))
        .filter(Holding.fund == symbol)
        .one()
    )


def get_etf_trades(db: Session, symbol: str, start_date: str, end_date: str):
    return (
        db.query(Trades)
        .filter(
            Trades.fund == symbol, Trades.date >= start_date, Trades.date <= end_date
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


def get_stock_fundownership(db: Session, symbol: str):
    subq = (
        db.query(Holding.fund, func.max(Holding.date).label("maxdate"))
        .group_by(Holding.fund)
        .subquery("t2")
    )

    return (
        db.query(Holding)
        .join(subq, and_(Holding.date == subq.c.maxdate))
        .filter(Holding.ticker == symbol)
        .all()
    )


def get_stock_fundownership_maxdate(db: Session, symbol: str):
    return (
        db.query(func.max(Holding.date).label("maxdate"))
        .filter(Holding.ticker == symbol)
        .first()
    )[0]


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
