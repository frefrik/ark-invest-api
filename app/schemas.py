import datetime
from typing import List, Optional
from pydantic import BaseModel


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
    fund: str
    date: datetime.date
    holdings: List[HoldingList] = []

    class Config:
        orm_mode = True


class TradeList(BaseModel):
    fund: str
    date: datetime.date
    direction: str
    ticker: Optional[str]
    cusip: str
    company: str
    shares: int
    etf_percent: float

    class Config:
        orm_mode = True


class FundTrades(BaseModel):
    fund: str
    date_from: datetime.date
    date_to: datetime.date
    trades: List[TradeList] = []

    class Config:
        orm_mode = True
