import datetime
from typing import List, Optional
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
        orm_mode = True


class FundProfile(BaseModel):
    profile: List[FundList] = []

    class Config:
        orm_mode = True


class HoldingList(BaseModel):
    company: str
    ticker: Optional[str]
    cusip: str
    shares: int
    market_value: float
    weight: float
    weight_rank: int

    class Config:
        orm_mode = True


class FundHolding(BaseModel):
    symbol: str
    date: datetime.date
    holdings: List[HoldingList] = []

    class Config:
        orm_mode = True


class TradeList(BaseModel):
    date: datetime.date
    direction: str
    ticker: Optional[str]
    company: str
    cusip: str
    shares: int
    etf_percent: float

    class Config:
        orm_mode = True


class FundTrades(BaseModel):
    symbol: str
    date_from: datetime.date
    date_to: datetime.date
    trades: List[TradeList] = []

    class Config:
        orm_mode = True


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

    class Config:
        orm_mode = True


class FundOwnershipList(BaseModel):
    fund: str
    weight: float
    weight_rank: int
    shares: int
    market_value: float

    class Config:
        orm_mode = True


class FundOwnership(BaseModel):
    symbol: str
    date: Optional[datetime.date]
    ownership: List[FundOwnershipList] = []
    totals: create_model(
        "totals", funds=(int, ...), shares=(int, ...), market_value=(float, ...)
    )

    class Config:
        orm_mode = True


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
        orm_mode = True


class StockTrades(BaseModel):
    symbol: str
    date_from: datetime.date
    date_to: datetime.date
    trades: List[StockTradesList]

    class Config:
        orm_mode = True


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
        orm_mode = True


class FundNews(BaseModel):
    symbol: Optional[str]
    date_from: datetime.date
    date_to: datetime.date
    news: List[FundNewsList] = []

    class Config:
        orm_mode = True
