import datetime
from typing import List, Optional

from pydantic import BaseModel


class FundProfileData(BaseModel):
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
    symbol: str
    profile: Optional[FundProfileData] = {}

    class Config:
        orm_mode = True


class FundHoldingData(BaseModel):
    date: datetime.date
    ticker: Optional[str]
    company: str
    cusip: str
    shares: int
    market_value: float
    weight: float
    weight_rank: int

    class Config:
        orm_mode = True


class FundHolding(BaseModel):
    symbol: str
    date_from: Optional[datetime.date]
    date_to: Optional[datetime.date]
    holdings: List[FundHoldingData] = []

    class Config:
        orm_mode = True


class FundTradeData(BaseModel):
    date: datetime.date
    ticker: Optional[str]
    company: str
    direction: str
    cusip: str
    shares: int
    etf_percent: float

    class Config:
        orm_mode = True


class FundTrades(BaseModel):
    symbol: str
    date_from: datetime.date = None
    date_to: datetime.date = None
    trades: List[FundTradeData] = []

    class Config:
        orm_mode = True


class FundOwnershipData(BaseModel):
    date: datetime.date
    fund: str
    weight: float
    weight_rank: int
    shares: int
    market_value: float

    class Config:
        orm_mode = True


class FundOwnershipTotals(BaseModel):
    funds: int
    shares: int
    market_value: float


class FundOwnershipList(BaseModel):
    date: datetime.date
    ownership: List[FundOwnershipData]
    totals: FundOwnershipTotals

    class Config:
        orm_mode = True


class FundOwnership(BaseModel):
    symbol: str
    date_from: Optional[datetime.date]
    date_to: Optional[datetime.date]
    data: List[FundOwnershipList] = []

    class Config:
        orm_mode = True


class FundNewsData(BaseModel):
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
    symbol: str
    date_from: Optional[datetime.date]
    date_to: Optional[datetime.date]
    news: List[FundNewsData] = []

    class Config:
        orm_mode = True


class StockProfileData(BaseModel):
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


class StockProfile(BaseModel):
    symbol: str
    profile: Optional[StockProfileData] = {}

    class Config:
        orm_mode = True


class StockTradeData(BaseModel):
    date: datetime.date
    fund: str
    direction: str
    shares: int
    etf_percent: float

    class Config:
        orm_mode = True


class StockTrades(BaseModel):
    symbol: str
    date_from: Optional[datetime.date]
    date_to: Optional[datetime.date]
    trades: List[StockTradeData] = []

    class Config:
        orm_mode = True
