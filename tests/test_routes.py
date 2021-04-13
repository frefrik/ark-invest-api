def test_etf_profile(client):
    response = client.get("/api/v1/etf/profile?symbol=ARKK")

    assert response.status_code == 200
    assert response.json() == {
        "profile": [
            {
                "symbol": "ARKK",
                "name": "ARK Innovation ETF",
                "description": "ARKK is an actively managed ETF that seeks long-term growth of capital by investing under normal circumstances primarily (at least 65% of its assets) in domestic and foreign equity securities of companies that are relevant to the Fund’s investment theme of disruptive innovation.",
                "fund_type": "Active Equity ETF",
                "inception_date": "2014-10-31",
                "cusip": "00214Q104",
                "isin": "US00214Q1040",
                "website": "https://ark-funds.com/arkk",
            }
        ]
    }


def test_etf_profile_inexistent_item(client):
    response = client.get("/api/v1/etf/profile?symbol=ARK")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Fund must be one of: ARKK, ARKQ, ARKW, ARKG, ARKF, ARKX, PRNT, IZRL"
    }


def test_etf_holdings(client):
    response = client.get("/api/v1/etf/holdings?symbol=ARKK")
    assert response.status_code == 200


def test_etf_holdings_inexistent_item(client):
    response = client.get("/api/v1/etf/holdings?symbol=ARK")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Symbol must be one of: ARKK, ARKQ, ARKW, ARKG, ARKF, ARKX, PRNT, IZRL"
    }


def test_etf_trades(client):
    response = client.get("/api/v1/etf/trades?symbol=ARKK")
    assert response.status_code == 200


def test_etf_trades_inexistent_item(client):
    response = client.get("/api/v1/etf/trades?symbol=ARK")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Fund must be one of: ARKK, ARKQ, ARKW, ARKG, ARKF, ARKX, PRNT, IZRL"
    }


def test_etf_news(client):
    response = client.get("/api/v1/etf/news")
    assert response.status_code == 200


def test_etf_news_inexistent_item(client):
    response = client.get("/api/v1/etf/news?symbol=TSLA")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Fund must be one of: ARKK, ARKQ, ARKW, ARKG, ARKF, ARKX, PRNT, IZRL"
    }


def test_stock_profile(client):
    response = client.get("/api/v1/stock/profile?symbol=TSLA")
    assert response.status_code == 200


def test_stock_profile_inexistent_item(client):
    response = client.get("/api/v1/stock/profile?symbol=TSLAS")
    assert response.status_code == 404
    assert response.json() == {"detail": "Ticker TSLAS not found."}


def test_stock_fund_ownership(client):
    response = client.get("/api/v1/stock/fund-ownership?symbol=TSLA")
    assert response.status_code == 200


def test_stock_fund_ownership_inexistent_item(client):
    response = client.get("/api/v1/stock/fund-ownership?symbol=TSLAS")
    assert response.status_code == 200
    assert response.json() == {
        "symbol": "TSLAS",
        "date": None,
        "ownership": [],
        "totals": {"funds": 0, "shares": 0, "market_value": 0.0},
    }


def test_stock_trades(client):
    response = client.get("/api/v1/stock/trades?symbol=TSLA")
    assert response.status_code == 200


def test_stock_trades_not_found(client):
    response = client.get("/api/v1/stock/trades?symbol=TSLAS")
    assert response.status_code == 404
    assert response.json() == {"detail": "No ARK trades found for TSLAS"}
