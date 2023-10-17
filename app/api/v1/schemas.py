import datetime
from typing import Optional

from pydantic import BaseModel, create_model


class FundList(BaseModel):
    symbol: str
    name: str
    description: str
    fund_type: str
    inception_date: datetime.date
    cusip: str
    isin: str
    website: str

    class Config:
        from_attributes = True


class FundProfile(BaseModel):
    profile: list[FundList] = []


class HoldingList(BaseModel):
    company: str
    ticker: Optional[str]
    cusip: str
    shares: int
    market_value: float
    weight: float
    weight_rank: int

    class Config:
        from_attributes = True


class FundHolding(BaseModel):
    symbol: str
    date: datetime.date
    holdings: list[HoldingList] = []


class TradeList(BaseModel):
    date: datetime.date
    direction: str
    ticker: Optional[str]
    company: str
    cusip: str
    shares: int
    etf_percent: float

    class Config:
        from_attributes = True


class FundTrades(BaseModel):
    symbol: str
    date_from: datetime.date
    date_to: datetime.date
    trades: list[TradeList] = []


class StockProfile(BaseModel):
    ticker: str
    name: Optional[str]
    country: Optional[str]
    industry: Optional[str]
    sector: Optional[str]
    fullTimeEmployees: Optional[int]
    summary: Optional[str]
    website: Optional[str]
    market: Optional[str]
    exchange: Optional[str]
    currency: Optional[str]
    marketCap: Optional[float]
    sharesOutstanding: Optional[int]


class FundOwnershipList(BaseModel):
    fund: str
    weight: float
    weight_rank: int
    shares: int
    market_value: float

    class Config:
        from_attributes = True


class FundOwnership(BaseModel):
    symbol: str
    date: Optional[datetime.date]
    ownership: list[FundOwnershipList] = []
    totals: create_model(
        "totals", funds=(int, ...), shares=(int, ...), market_value=(float, ...)
    )


class StockTradesList(BaseModel):
    date: datetime.date
    fund: str
    direction: str
    ticker: str
    company: str
    cusip: str
    shares: int
    etf_percent: float

    class Config:
        from_attributes = True


class StockTrades(BaseModel):
    symbol: str
    date_from: datetime.date
    date_to: datetime.date
    trades: list[StockTradesList]


class FundNewsList(BaseModel):
    id: int
    datetime: datetime.datetime
    related: str
    source: str
    headline: str
    summary: str
    url: str
    image: str

    class Config:
        from_attributes = True


class FundNews(BaseModel):
    symbol: Optional[str]
    date_from: datetime.date
    date_to: datetime.date
    news: list[FundNewsList] = []
