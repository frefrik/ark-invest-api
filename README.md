# ARK Invest API

## Documentation

Swagger UI: <https://arkfunds.io/api>  
ReDoc: <https://arkfunds.io/api/docs>

## Endpoints

- **[<code>GET</code> ETF Profile](#etf-profile)**
- **[<code>GET</code> ETF Holdings](#etf-holdings)**
- **[<code>GET</code> ETF Trades](#etf-trades)**
- **[<code>GET</code> ETF News](#etf-news)**
- **[<code>GET</code> Stock Profile](#stock-profile)**
- **[<code>GET</code> Stock Trades](#stock-trades)**
- **[<code>GET</code> Stock Fund Ownership](#stock-fund-ownership)**

## ETF Profile

    GET /v1/etf/profile

Returns ARK ETF profile information

### Query Parameters

| Parameter | Required | Valid values                                   | Default value |
| --------- | :------: | ---------------------------------------------- | ------------- |
| symbol    |    NO    | ARKK, ARKQ, ARKW, ARKG, ARKF, ARKX, PRNT, IZRL |               |

### Example

#### Request

    GET https://arkfunds.io/api/v1/etf/profile?symbol=ARKK

#### Response

``` json
{
    "profile": [{
        "symbol": "ARKK",
        "name": "ARK Innovation ETF",
        "description": "ARKK is an actively managed ETF that seeks long-term growth of capital by investing under normal circumstances primarily (at least 65% of its assets) in domestic and foreign equity securities of companies that are relevant to the Fund’s investment theme of disruptive innovation.",
        "fund_type": "Active Equity ETF",
        "inception_date": "2014-10-31",
        "cusip": "00214Q104",
        "isin": "US00214Q1040",
        "website": "https://ark-funds.com/arkk"
    }]
}
```

## ETF Holdings

    GET /v1/etf/holdings

Returns ARK ETF holdings

### Query Parameters

| Parameter | Required | Valid values                                   | Default value |
| --------- | :------: | ---------------------------------------------- | ------------- |
| symbol    |   YES    | ARKK, ARKQ, ARKW, ARKG, ARKF, ARKX, PRNT, IZRL |               |
| date      |    NO    | ISO 8601 Calendar date                         |               |

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

## ETF Trades

    GET /v1/etf/trades

Returns ARK ETF intraday trades

### Query Parameters

| Parameter | Required | Valid values                       | Default value |
| --------- | :------: | ---------------------------------- | ------------- |
| symbol    |   YES    | ARKK, ARKQ, ARKW, ARKG, ARKF, ARKX |               |
| period    |    NO    | 1d, 7d, 1m, 3m, 1y, ytd            | 1d            |

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

## ETF News

    GET /v1/etf/news

Returns ARK ETF news

### Query Parameters

| Parameter | Required | Valid values                                   | Default value |
| --------- | :------: | ---------------------------------------------- | ------------- |
| symbol    |    NO    | ARKK, ARKQ, ARKW, ARKG, ARKF, ARKX, PRNT, IZRL |               |
| date      |    NO    | ISO 8601 Calendar date                         |               |
| date_to   |    NO    | ISO 8601 Calendar date                         |               |

### Example

#### Request

    GET https://arkfunds.io/api/v1/etf/news?symbol=ARKG&date_from=2021-03-31&date_to=2021-04-02

#### Response

``` json
{
  "symbol": "ARKG",
  "date_from": "2021-03-31",
  "date_to": "2021-04-02",
  "news": [
    {
      "id": 42,
      "datetime": "2021-04-02T07:27:32+00:00",
      "related": "ARKG",
      "source": "seekingalpha.com",
      "headline": "ARK Genomic Revolution Multi-Sector ETF: Poised For Continued Underperformance",
      "summary": "I am neutral on the ETF. For short-term gains, investors may wish to look elsewhere.",
      "url": "https://seekingalpha.com/article/4417325-ark-genomic-revolution-multi-sector-etf-underperformance",
      "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/842211270/medium_image_842211270.jpg"
    },
    {
      "id": 568,
      "datetime": "2021-03-31T22:53:00+00:00",
      "related": "ARKG",
      "source": "Benzinga",
      "headline": "Pinduoduo, Shopify PayPal, LendingTree, JD.com — What Cathy Wood's Ark Bought And Sold On Wednesday",
      "summary": "Cathie Wood’s Ark Investment Management sends out an email every night listing the stocks that were bought or sold by the firm's ETFs that day. In recent months, the...",
      "url": "https://www.benzinga.com/news/21/03/20438462/pinduoduo-shopify-paypal-lendingtree-jd-com-what-cathy-woods-ark-bought-and-sold-on-wednesday",
      "image": "https://cdn.benzinga.com/files/imagecache/og_image_social_share_1200x630/images/story/2012/micheile-henderson-lz_4npfkcv8-unsplash_7.jpg"
    },
    {
      "id": 569,
      "datetime": "2021-03-31T12:05:09+00:00",
      "related": "ARKG",
      "source": "DowJones",
      "headline": "UPDATE: Fauci says vaccines are offering protection against new, more infectious COVID variants",
      "summary": "Dr. Anthony Fauci, head of the National Institute of Allergy and Infectious Diseases and President Joe Biden's chief medical officer, said Wednesday the...",
      "url": "https://www.marketwatch.com/story/white-house-coronavirus-team-says-90-of-american-adults-will-be-eligible-for-vaccine-by-april-19-2021-03-31",
      "image": "https://s.wsj.net/public/resources/MWimages/MW-GP644_MicroS_ZG_20180906154215.jpg"
    },
    {
      "id": 570,
      "datetime": "2021-03-31T11:01:00+00:00",
      "related": "ARKG",
      "source": "DowJones",
      "headline": "Russia registers ‘world’s first’ COVID-19 vaccine for dogs, cats and other animals",
      "summary": "Russia has registered the world’s first COVID-19 vaccine for animals, the country’s agricultural regulator said on Wednesday.",
      "url": "https://www.marketwatch.com/story/russia-registers-worlds-first-covid-19-vaccine-for-animals-11617202893",
      "image": "https://images.mktw.net/im-318622/social"
    }
  ]
}
```

## Stock Profile

    GET /v1/stock/profile

Returns Stock profile information

### Query Parameters

| Parameter | Required | Valid values | Default value |
| --------- | :------: | ------------ | ------------- |
| symbol    |   YES    |              |               |

### Example

#### Request

    GET https://arkfunds.io/api/v1/stock/profile?symbol=TSLA

#### Response

``` json
{
  "ticker": "TSLA",
  "name": "Tesla, Inc.",
  "country": "United States",
  "industry": "Auto Manufacturers",
  "sector": "Consumer Cyclical",
  "fullTimeEmployees": 48016,
  "summary": "Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems in the United States, China, Netherlands, Norway, and internationally. The company operates in two segments, Automotive; and Energy Generation and Storage. The Automotive segment offers sedans and sport utility vehicles. It also provides electric powertrain components and systems; and services for electric vehicles through its company-owned service locations, and Tesla mobile service technicians, as well as sells used vehicles. This segment markets and sells its products through a network of company-owned stores and galleries, as well as through its own Website. The Energy Generation and Storage segment offers energy storage products, such as rechargeable lithium-ion battery systems for use in homes, industrial, commercial facilities, and utility grids; and designs, manufactures, installs, maintains, leases, and sells solar energy generation and energy storage products to residential and commercial customers. It also provides vehicle insurance services, as well as renewable energy. The company was formerly known as Tesla Motors, Inc. and changed its name to Tesla, Inc. in February 2017. Tesla, Inc. was founded in 2003 and is headquartered in Palo Alto, California.",
  "website": "http://www.tesla.com",
  "market": "us_market",
  "exchange": "NasdaqGS",
  "currency": "USD",
  "marketCap": 783117844480,
  "sharesOutstanding": 947900992
}
```

## Stock Trades

    GET /v1/stock/trades

Returns Stock Trades

### Query Parameters

| Parameter | Required | Valid values           | Default value |
| --------- | :------: | ---------------------- | ------------- |
| symbol    |   YES    |                        |               |
| direction |    NO    | buy, sell              |               |
| date_from |    NO    | ISO 8601 Calendar date |               |
| date_to   |    NO    | ISO 8601 Calendar date |               |

### Example

#### Request

    GET https://arkfunds.io/api/v1/stock/trades?symbol=TSLA

#### Response

``` json
{
    "symbol": "TSLA",
    "date_from": "2020-09-18",
    "date_to": "2021-01-12",
    "trades": [{
        "date": "2021-01-12",
        "fund": "ARKK",
        "direction": "Sell",
        "ticker": "TSLA",
        "company": "TESLA INC",
        "cusip": "88160R101",
        "shares": 126276,
        "etf_percent": 0.5055
    }, {
        "date": "2021-01-12",
        "fund": "ARKQ",
        "direction": "Sell",
        "ticker": "TSLA",
        "company": "TESLA INC",
        "cusip": "88160R101",
        "shares": 13179,
        "etf_percent": 0.4991
    }, {
        "date": "2021-01-12",
        "fund": "ARKW",
        "direction": "Sell",
        "ticker": "TSLA",
        "company": "TESLA INC",
        "cusip": "88160R101",
        "shares": 16898,
        "etf_percent": 0.6161
    }, {
        "date": "2021-01-08",
        "fund": "ARKK",
        "direction": "Sell",
        "ticker": "TSLA",
        "company": "TESLA INC",
        "cusip": "88160R101",
        "shares": 59500,
        "etf_percent": 0.2506
    }]
}
```

## Stock Fund Ownership

    GET /v1/stock/fund-ownership

Returns Stock Fund Ownership

### Query Parameters

| Parameter | Required | Valid values | Default value |
| --------- | :------: | ------------ | ------------- |
| symbol    |   YES    |              |               |

### Example

#### Request

    GET https://arkfunds.io/api/v1/stock/fund-ownership?symbol=TSLA

#### Response

``` json
{
    "symbol": "TSLA",
    "date": "2021-01-15",
    "ownership": [{
        "fund": "ARKK",
        "weight": 9.65,
        "weight_rank": 1,
        "shares": 2626774,
        "market_value": 2170135607.84
    }, {
        "fund": "ARKQ",
        "weight": 11.37,
        "weight_rank": 1,
        "shares": 335957,
        "market_value": 277554235.12
    }, {
        "fund": "ARKW",
        "weight": 9.87,
        "weight_rank": 1,
        "shares": 734796,
        "market_value": 607059063.36
    }],
    "totals": {
        "funds": 3,
        "shares": 3697527,
        "market_value": 3054748906.32
    }
}
```
