from sqlalchemy import Column, Integer, String, Date, Float
from .database import Base


class Fund(Base):
    __tablename__ = "funds"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String)
    name = Column(String)
    description = Column(String)
    cusip = Column(String)
    isin = Column(String)
    inception_date = Column(Date)
    website = Column(String)
    fund_type = Column(String)


class Holding(Base):
    __tablename__ = "holdings"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    fund = Column(String)
    company = Column(String)
    ticker = Column(String, nullable=True)
    cusip = Column(String)
    shares = Column(Integer)
    market_value = Column(Float)
    weight = Column(Float)
    weight_rank = Column(Integer)


class Trades(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    fund = Column(String)
    direction = Column(String)
    ticker = Column(String, nullable=True)
    cusip = Column(String)
    company = Column(String)
    shares = Column(Integer, nullable=True)
    etf_percent = Column(Float, nullable=True)


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    external_id = Column(Integer, index=True, unique=True)
    datetime = Column(Integer)
    category = Column(String)
    related = Column(String)
    source = Column(String)
    headline = Column(String)
    summary = Column(String)
    url = Column(String)
    image = Column(String)
