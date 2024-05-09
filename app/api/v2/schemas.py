import datetime
from typing import Optional

from pydantic import BaseModel


class V2_FundProfileData(BaseModel):
    symbol: str
    name: str
    description: str
    fund_type: str
    inception_date: datetime.date
    cusip: str | None
    isin: str | None
    website: str

    class Config:
        from_attributes = True


class V2_FundProfile(BaseModel):
    symbol: str
    profile: Optional[V2_FundProfileData] = {}


class V2_FundHoldingData(BaseModel):
    fund: str
    date: datetime.date
    ticker: str | None = None
    company: str
    cusip: str | None = None
    shares: int | None = None
    market_value: float | None = None
    share_price: float | None = None
    weight: float
    weight_rank: int | None = None

    class Config:
        from_attributes = True


class V2_FundHolding(BaseModel):
    symbol: str
    date_from: datetime.date | None = None
    date_to: datetime.date | None = None
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
    value: float | str | None = None


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
    ticker: str | None = None
    company: str
    direction: str
    cusip: str
    shares: int
    etf_percent: float

    class Config:
        from_attributes = True


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
        from_attributes = True


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
    date_from: datetime.date | None = None
    date_to: datetime.date | None = None
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
        from_attributes = True


class V2_FundNews(BaseModel):
    symbol: str
    date_from: datetime.date | None = None
    date_to: datetime.date | None = None
    news: list[V2_FundNewsData] = []


class V2_StockProfileData(BaseModel):
    ticker: str
    name: str | None = None
    country: str | None = None
    industry: str | None = None
    sector: str | None = None
    fullTimeEmployees: int | None = None
    summary: str | None = None
    website: str | None = None
    market: str | None = None
    exchange: str | None = None
    currency: str | None = None
    marketCap: float | None = None
    sharesOutstanding: int | None = None
    price: float | None = None
    change: float | None = None
    changep: float | None = None
    last_trade: datetime.datetime | None = None


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
        from_attributes = True


class V2_StockTrades(BaseModel):
    symbol: str
    date_from: datetime.date | None = None
    date_to: datetime.date | None = None
    trades: list[V2_StockTradeData] = []


class V2_StockPrice(BaseModel):
    symbol: str
    exchange: str | None = None
    currency: str | None = None
    price: float | None = None
    change: float | None = None
    changep: float | None = None
    last_trade: datetime.datetime | None = None
