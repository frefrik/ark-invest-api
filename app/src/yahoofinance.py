import json
from datetime import datetime

import requests


class YahooFinance:
    API_URL = "https://query1.finance.yahoo.com"
    DEFAULT_TIMEOUT = 10

    def __init__(self, symbol):
        self.symbol = symbol
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0"
        }

    def _request(self, method, path, **kwargs):
        uri = "{}/{}".format(self.API_URL, path)
        params = self._format_params(kwargs.get("params", {}))

        response = getattr(requests, method)(
            uri,
            headers=self.headers,
            params=params,
            timeout=self.DEFAULT_TIMEOUT,
        )

        if response.status_code != 200:
            return None

        return response.json()

    @staticmethod
    def _format_params(params):
        return {k: json.dumps(v) if isinstance(v, bool) else v for k, v in params.items()}

    def _get(self, path, **kwargs):
        return self._request("get", path, **kwargs)

    def _get_price(self):
        return self._get_quoteSummary("price")

    def _get_key_stats(self):
        return self._get_quoteSummary("defaultKeyStatistics")

    def _get_quoteSummary(self, module):
        res = self._get(
            f"/v10/finance/quoteSummary/{self.symbol}",
            params={"modules": module},
        )

        if res:
            _json = res["quoteSummary"]["result"]

            if len(_json) > 0:
                return _json[0][module]
            else:
                return None

    @property
    def fund_performance(self):
        return self._get_quoteSummary("fundPerformance")

    @property
    def quote(self):
        data = {}
        profile = self._get_quoteSummary("assetProfile")
        price = self._get_price()
        key_stats = self._get_key_stats()

        if profile:
            data["country"] = profile.get("country")
            data["industry"] = profile.get("industry")
            data["sector"] = profile.get("sector")
            data["fullTimeEmployees"] = profile.get("fullTimeEmployees")
            data["summary"] = profile.get("longBusinessSummary")
            data["website"] = profile.get("website")

        if price:
            data["name"] = price.get("longName")
            data["currency"] = price.get("currency")
            data["exchange"] = price.get("exchangeName")
            data["currency"] = price.get("currency")
            data["marketCap"] = price.get("marketCap", {}).get("raw")

        if key_stats:
            data["sharesOutstanding"] = key_stats.get("sharesOutstanding", {}).get("raw")

        return data

    @property
    def price(self):
        data = {}
        quote = self._get_price()

        if quote:
            data["exchange"] = quote.get("exchangeName")
            data["currency"] = quote.get("currency")
            data["price"] = quote.get("regularMarketPrice", {}).get("raw")
            data["change"] = quote.get("regularMarketChange", {}).get("raw")
            data["changep"] = quote.get("regularMarketChangePercent", {}).get("raw")
            data["last_trade"] = datetime.utcfromtimestamp(quote.get("regularMarketTime"))

        return data
