import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, create_model


class FundList(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    symbol: str
    name: str
    description: str
    fund_type: str
    inception_date: datetime.date
    cusip: str
    isin: str
    website: str


class FundProfile(BaseModel):
    profile: list[FundList] = []


class HoldingList(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    company: str
    ticker: Optional[str]
    cusip: Optional[str]
    shares: Optional[int]
    market_value: Optional[float]
    weight: float
    weight_rank: int


class FundHolding(BaseModel):
    symbol: str
    date: datetime.date
    holdings: list[HoldingList] = []


class TradeList(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    date: datetime.date
    direction: str
    ticker: Optional[str]
    company: str
    cusip: str
    shares: int
    etf_percent: float


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
    model_config = ConfigDict(from_attributes=True)

    fund: str
    weight: float
    weight_rank: int
    shares: int
    market_value: float


class FundOwnership(BaseModel):
    symbol: str
    date: Optional[datetime.date]
    ownership: list[FundOwnershipList] = []
    totals: create_model("totals", funds=(int, ...), shares=(int, ...), market_value=(float, ...))


class StockTradesList(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    date: datetime.date
    fund: str
    direction: str
    ticker: str
    company: str
    cusip: str
    shares: int
    etf_percent: float


class StockTrades(BaseModel):
    symbol: str
    date_from: datetime.date
    date_to: datetime.date
    trades: list[StockTradesList]


class FundNewsList(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    datetime: datetime.datetime
    related: str
    source: str
    headline: str
    summary: str
    url: str
    image: str


class FundNews(BaseModel):
    symbol: Optional[str]
    date_from: datetime.date
    date_to: datetime.date
    news: list[FundNewsList] = []
