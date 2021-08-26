import datetime
from typing import List, Optional

from pydantic import BaseModel


class V2_FundProfileData(BaseModel):
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


class V2_FundProfile(BaseModel):
    symbol: str
    profile: Optional[V2_FundProfileData] = {}

    class Config:
        orm_mode = True


class V2_FundHoldingData(BaseModel):
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


class V2_FundHolding(BaseModel):
    symbol: str
    date_from: Optional[datetime.date]
    date_to: Optional[datetime.date]
    holdings: List[V2_FundHoldingData] = []

    class Config:
        orm_mode = True


class V2_FundTradeData(BaseModel):
    date: datetime.date
    ticker: Optional[str]
    company: str
    direction: str
    cusip: str
    shares: int
    etf_percent: float

    class Config:
        orm_mode = True


class V2_FundTrades(BaseModel):
    symbol: str
    date_from: datetime.date = None
    date_to: datetime.date = None
    trades: List[V2_FundTradeData] = []

    class Config:
        orm_mode = True


class V2_FundOwnershipData(BaseModel):
    date: datetime.date
    fund: str
    weight: float
    weight_rank: int
    shares: int
    market_value: float

    class Config:
        orm_mode = True


class V2_FundOwnershipTotals(BaseModel):
    funds: int
    shares: int
    market_value: float


class V2_FundOwnershipList(BaseModel):
    date: datetime.date
    ownership: List[V2_FundOwnershipData]
    totals: V2_FundOwnershipTotals

    class Config:
        orm_mode = True


class V2_FundOwnership(BaseModel):
    symbol: str
    date_from: Optional[datetime.date]
    date_to: Optional[datetime.date]
    data: List[V2_FundOwnershipList] = []

    class Config:
        orm_mode = True


class V2_FundNewsData(BaseModel):
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


class V2_FundNews(BaseModel):
    symbol: str
    date_from: Optional[datetime.date]
    date_to: Optional[datetime.date]
    news: List[V2_FundNewsData] = []

    class Config:
        orm_mode = True


class V2_StockProfileData(BaseModel):
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


class V2_StockProfile(BaseModel):
    symbol: str
    profile: Optional[V2_StockProfileData] = {}

    class Config:
        orm_mode = True


class V2_StockTradeData(BaseModel):
    date: datetime.date
    fund: str
    direction: str
    shares: int
    etf_percent: float

    class Config:
        orm_mode = True


class V2_StockTrades(BaseModel):
    symbol: str
    date_from: Optional[datetime.date]
    date_to: Optional[datetime.date]
    trades: List[V2_StockTradeData] = []

    class Config:
        orm_mode = True
