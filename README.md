# ARK Invest API

## Documentation
Swagger UI: https://arkfunds.io/api  
ReDoc: https://arkfunds.io/api/docs


## Endpoints
- **[<code>GET</code> ARK ETF metadata](#Funds)**
- **[<code>GET</code> ARK ETF holdings](#Holdings)**
- **[<code>GET</code> ARK ETF intraday trades](#Trades)**


## Funds

    GET /etf/profile

Returns ARK ETF profile information

### Query Parameters
Parameter | Valid values | Default value
--- | --- | ---
symbol | ARKK, ARKQ, ARKW, ARKG, ARKF | 

### Example
#### Request

    GET https://arkfunds.io/api/v1/etf/profile?symbol=ARKK

#### Response
``` json
{
    "profile": [{
        "symbol": "ARKK",
        "name": "ARK Innovation ETF",
        "description": "ARKK is an actively managed ETF that seeks long-term growth of capital by investing under normal circumstances primarily (at least 65% of its assets) in domestic and foreign equity securities of companies that are relevant to the Fund’s investment theme of disruptive innovation."
    }]
}
```

## Holdings

    GET /etf/holdings

Returns ARK ETF holdings

### Query Parameters
Parameter | Valid values | Default value
--- | --- | ---
symbol | ARKK, ARKQ, ARKW, ARKG, ARKF | 

### Example
#### Request

    GET https://arkfunds.io/api/v1/etf/holdings?symbol=ARKK

#### Response
``` json
{
    "symbol": "ARKK",
    "date": "2021-01-15",
    "holdings": [{
        "company": "TESLA INC",
        "ticker": "TSLA",
        "cusip": "88160R101",
        "shares": 2626774,
        "market_value": 2170135607.84,
        "weight": 9.65,
        "weight_rank": 1
    }, {
        "company": "ROKU INC",
        "ticker": "ROKU",
        "cusip": "77543R102",
        "shares": 4110728,
        "market_value": 1678410242.4,
        "weight": 7.47,
        "weight_rank": 2
    }, {
        "company": "CRISPR THERAPEUTICS AG",
        "ticker": "CRSP",
        "cusip": "H17182108",
        "shares": 6246733,
        "market_value": 1248596992.04,
        "weight": 5.55,
        "weight_rank": 3
    }, {
        "company": "SQUARE INC - A",
        "ticker": "SQ",
        "cusip": "852234103",
        "shares": 4776169,
        "market_value": 1087772489.75,
        "weight": 4.84,
        "weight_rank": 4
    }, {
        "company": "TELADOC HEALTH INC",
        "ticker": "TDOC",
        "cusip": "87918A105",
        "shares": 4325169,
        "market_value": 974244317.25,
        "weight": 4.33,
        "weight_rank": 5
    }]
}
```

## Trades

    GET /etf/trades

Returns ARK ETF intraday trades

### Query Parameters
Parameter | Valid values | Default value
--- | --- | ---
symbol | ARKK, ARKQ, ARKW, ARKG, ARKF | 
period | 1d, 7d, 1m, 3m, 1y, ytd | 1d


### Example
#### Request

    GET https://arkfunds.io/api/v1/etf/trades?symbol=ARKK

#### Response
``` json
{
    "symbol": "ARKK",
    "date_from": "2021-01-15",
    "date_to": "2021-01-15",
    "trades": [{
        "fund": "ARKK",
        "date": "2021-01-15",
        "direction": "Buy",
        "ticker": "REGN",
        "cusip": "75886F107",
        "company": "REGENERON PHARMACEUTICALS INC",
        "shares": 81933,
        "etf_percent": 0.191
    }, {
        "fund": "ARKK",
        "date": "2021-01-15",
        "direction": "Buy",
        "ticker": "SPOT",
        "cusip": "L8681T102",
        "company": "SPOTIFY TECHNOLOGY SA",
        "shares": 88270,
        "etf_percent": 0.1269
    }, {
        "fund": "ARKK",
        "date": "2021-01-15",
        "direction": "Buy",
        "ticker": "TXG",
        "cusip": "88025U109",
        "company": "10X GENOMICS INC",
        "shares": 53881,
        "etf_percent": 0.0434
    }, {
        "fund": "ARKK",
        "date": "2021-01-15",
        "direction": "Buy",
        "ticker": "SNPS",
        "cusip": "871607107",
        "company": "SYNOPSYS INC",
        "shares": 26425,
        "etf_percent": 0.0309
    }]
}
```
