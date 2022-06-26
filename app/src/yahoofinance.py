import json
from datetime import datetime

import requests


class YahooFinance:
    API_URL = "https://query1.finance.yahoo.com"
    DEFAULT_TIMEOUT = 10

    def __init__(self, symbol):
        self.symbol = symbol
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0"
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
        return {
            k: json.dumps(v) if isinstance(v, bool) else v for k, v in params.items()
        }

    def _get(self, path, **kwargs):
        return self._request("get", path, **kwargs)

    def _get_quote(self):
        res = self._get("/v7/finance/quote", params={"symbols": self.symbol})

        if res:
            _json = res["quoteResponse"]["result"]

            if len(_json) > 0:
                return _json[0]
            else:
                return None

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
