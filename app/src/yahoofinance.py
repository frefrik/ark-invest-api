from datetime import datetime

import requests


class YahooFinance:
    QUOTE_URL = "https://query1.finance.yahoo.com/v7/finance/quote?symbols={0}"
    PROFILE_URL = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{0}?modules=assetProfile"

    def __init__(self, symbol):
        self.symbol = symbol
        self.timeout = 2
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0"
            }
        )

    def _get(self, url, params=None):
        res = self.session.get(url, params=params, timeout=self.timeout)

        if res.status_code == 404:
            return None
        elif res.status_code == 400:
            return None

        res.raise_for_status()

        return res

    def _get_quote(self):
        res = self._get(self.QUOTE_URL.format(self.symbol))

        if res:
            _json = res.json()["quoteResponse"]["result"]

            if len(_json) > 0:
                return _json[0]
            else:
                return None

    def _get_asset_profile(self):
        res = self._get(self.PROFILE_URL.format(self.symbol))

        if res:
            _json = res.json()["quoteSummary"]["result"]

            if len(_json) > 0:
                return _json[0]["assetProfile"]
            else:
                return None

    @property
    def quote(self):
        data = {}
        profile = self._get_asset_profile()
        quote = self._get_quote()

        if profile:
            data["country"] = profile.get("country")
            data["industry"] = profile.get("industry")
            data["sector"] = profile.get("sector")
            data["fullTimeEmployees"] = profile.get("fullTimeEmployees")
            data["summary"] = profile.get("longBusinessSummary")
            data["website"] = profile.get("website")

        if quote:
            data["name"] = quote.get("longName")
            data["currency"] = quote.get("currency")
            data["market"] = quote.get("market")
            data["exchange"] = quote.get("fullExchangeName")
            data["currency"] = quote.get("currency")
            data["marketCap"] = quote.get("marketCap")
            data["sharesOutstanding"] = quote.get("sharesOutstanding")

        return data

    @property
    def price(self):
        data = {}
        quote = self._get_quote()

        if quote:
            data["exchange"] = quote.get("fullExchangeName")
            data["currency"] = quote.get("currency")
            data["price"] = quote.get("regularMarketPrice")
            data["change"] = quote.get("regularMarketChange")
            data["changep"] = quote.get("regularMarketChangePercent")
            data["last_trade"] = datetime.utcfromtimestamp(
                quote.get("regularMarketTime")
            )

        return data
