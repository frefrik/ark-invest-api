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

    def _get_data(self, url, params=None):
        res = self.session.get(url, params=params, timeout=self.timeout)

        if res.status_code == 404:
            return None

        res.raise_for_status()

        return res

    @property
    def quote(self):
        data = {}
        profile = self._get_data(self.PROFILE_URL.format(self.symbol))
        quote = self._get_data(self.QUOTE_URL.format(self.symbol))

        if profile:
            profile_json = profile.json()["quoteSummary"]["result"]

            if len(profile_json) > 0:
                profile_data = profile_json[0]["assetProfile"]

                data["country"] = profile_data.get("country")
                data["industry"] = profile_data.get("industry")
                data["sector"] = profile_data.get("sector")
                data["fullTimeEmployees"] = profile_data.get("fullTimeEmployees")
                data["summary"] = profile_data.get("longBusinessSummary")
                data["website"] = profile_data.get("website")

        if quote:
            quotejson = quote.json()["quoteResponse"]["result"]

            if len(quotejson) > 0:
                quote_data = quotejson[0]

                data["name"] = quote_data.get("longName")
                data["currency"] = quote_data.get("currency")
                data["market"] = quote_data.get("market")
                data["exchange"] = quote_data.get("fullExchangeName")
                data["currency"] = quote_data.get("currency")
                data["marketCap"] = quote_data.get("marketCap")
                data["sharesOutstanding"] = quote_data.get("sharesOutstanding")

        return data
