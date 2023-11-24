from yahooquery import Ticker


class YahooFinance:
    def __init__(self, symbol, formatted=False):
        self.symbol = symbol

        if formatted:
            self.ticker = Ticker(self.symbol, formatted="True")
        else:
            self.ticker = Ticker(self.symbol)

    @property
    def fund_performance(self):
        return self.ticker.fund_performance[self.symbol]

    @property
    def quote(self):
        data = {}
        profile = self.ticker.asset_profile[self.symbol]
        price = self.ticker.price[self.symbol]
        key_stats = self.ticker.key_stats[self.symbol]

        if "Quote not found" not in profile:
            data["country"] = profile.get("country")
            data["industry"] = profile.get("industry")
            data["sector"] = profile.get("sector")
            data["fullTimeEmployees"] = profile.get("fullTimeEmployees")
            data["summary"] = profile.get("longBusinessSummary")
            data["website"] = profile.get("website")

        if "Quote not found" not in price:
            data["name"] = price.get("longName")
            data["currency"] = price.get("currency")
            data["exchange"] = price.get("exchangeName")
            data["currency"] = price.get("currency")
            data["marketCap"] = price.get("marketCap")

        if "Quote not found" not in key_stats:
            data["sharesOutstanding"] = key_stats.get("sharesOutstanding")

        return data

    @property
    def price(self):
        data = {}
        price = self.ticker.price[self.symbol]

        if price:
            data["exchange"] = price.get("exchangeName")
            data["currency"] = price.get("currency")
            data["price"] = price.get("regularMarketPrice")
            data["change"] = price.get("regularMarketChange")
            data["changep"] = price.get("regularMarketChangePercent")
            data["last_trade"] = price.get("regularMarketTime")

        return data
