import datetime
from typing import Optional

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


class V2_FundHoldingData(BaseModel):
    fund: str
    date: datetime.date
    ticker: Optional[str]
    company: str
    cusip: str
    shares: int
    market_value: float
    share_price: float
    weight: float
    weight_rank: int


class V2_FundHolding(BaseModel):
    symbol: str
    date_from: Optional[datetime.date]
    date_to: Optional[datetime.date]
    holdings: list[V2_FundHoldingData] = []


class V2_FundPerformanceOverview(BaseModel):
    asOfDate: datetime.date | int
    ytdReturn: float | str | None = None
    oneYearReturn: float | str | None = None
    threeYearReturn: float | str | None = None


class V2_FundTrailingReturns(BaseModel):
    asOfDate: datetime.date | int
    ytd: float | str | None = None
    oneMonth: float | str | None = None
    threeMonth: float | str | None = None
    oneYear: float | str | None = None
    threeYear: float | str | None = None
    fiveYear: float | str | None = None
    tenYear: float | str | None = None


class V2_FundAnnualReturns(BaseModel):
    year: str
    value: float | str | None = 0


class V2_FundPerformanceData(BaseModel):
    fund: str
    overview: V2_FundPerformanceOverview
    trailingReturns: V2_FundTrailingReturns
    annualReturns: list[V2_FundAnnualReturns]


class V2_FundPerformance(BaseModel):
    symbol: str
    performance: list[V2_FundPerformanceData] = []


class V2_FundTradeData(BaseModel):
    fund: str
    date: datetime.date
    ticker: Optional[str]
    company: str
    direction: str
    cusip: str
    shares: int
    etf_percent: float


class V2_FundTrades(BaseModel):
    symbol: str
    date_from: datetime.date | None = None
    date_to: datetime.date | None = None
    trades: list[V2_FundTradeData] = []


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
    ownership: list[V2_FundOwnershipData]
    totals: V2_FundOwnershipTotals


class V2_FundOwnership(BaseModel):
    symbol: str
    date_from: Optional[datetime.date]
    date_to: Optional[datetime.date]
    data: list[V2_FundOwnershipList] = []


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
    news: list[V2_FundNewsData] = []


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
    price: Optional[float]
    change: Optional[float]
    changep: Optional[float]
    last_trade: Optional[datetime.datetime]


class V2_StockProfile(BaseModel):
    symbol: str
    profile: Optional[V2_StockProfileData] = {}


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
    trades: list[V2_StockTradeData] = []


class V2_StockPrice(BaseModel):
    symbol: str
    exchange: Optional[str]
    currency: Optional[str]
    price: Optional[float]
    change: Optional[float]
    changep: Optional[float]
    last_trade: Optional[datetime.datetime]
