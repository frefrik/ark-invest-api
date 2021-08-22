# ARK Invest API

API for tracking holdings and trades of [ARK Invest funds](https://ark-funds.com/).

Endpoint Status: https://status.arkfunds.io

<details>
<summary>
Click here to see a list of ARK ETFs
</summary>

**Active ETFs**
- **ARKK** - ARK Innovation ETF
- **ARKQ** - Autonomous Technology & Robotics ETF
- **ARKW** - Next Generation Internet ETF
- **ARKG** - Genomic Revolution ETF
- **ARKF** - Fintech Innovation ETF
- **ARKX** - Space Exploration & Innovation ETF

**Index ETFs**
- **PRNT** - The 3D Printing ETF
- **IZRL** - Israel Innovative Technology ETF
</details>

## Documentation

Swagger UI: <https://arkfunds.io/api>  
ReDoc: <https://arkfunds.io/api/docs>

## Endpoints

<details open>
<summary>
<b>V2</b>
</summary>

- **[<code>GET</code> ETF Profile](#etf-profile-v2)**
- **[<code>GET</code> ETF Holdings](#etf-holdings-v2)**
- **[<code>GET</code> ETF Trades](#etf-trades-v2)**
- **[<code>GET</code> ETF News](#etf-news-v2)**
- **[<code>GET</code> Stock Profile](#stock-profile-v2)**
- **[<code>GET</code> Stock Trades](#stock-trades-v2)**
- **[<code>GET</code> Stock Fund Ownership](#stock-fund-ownership-v2)**
</details>

<details>
<summary>
<b>V1</b>
</summary>

- **[<code>GET</code> ETF Profile](#etf-profile-v1)**
- **[<code>GET</code> ETF Holdings](#etf-holdings-v1)**
- **[<code>GET</code> ETF Trades](#etf-trades-v1)**
- **[<code>GET</code> ETF News](#etf-news-v1)**
- **[<code>GET</code> Stock Profile](#stock-profile-v1)**
- **[<code>GET</code> Stock Trades](#stock-trades-v1)**
- **[<code>GET</code> Stock Fund Ownership](#stock-fund-ownership-v1)**
</details>

## ETF Profile (v2)

    GET /v2/etf/profile

Returns ARK ETF profile information

### Query Parameters

| Parameter | Required | Description    |
| --------- | :------: | -------------- |
| symbol    |   YES    | ARK ETF symbol |

### Example

#### Request

    GET https://arkfunds.io/api/v2/etf/profile?symbol=ARKK

#### Response

``` json
{
    "symbol": "ARKK",
    "profile": {
        "symbol": "ARKK",
        "name": "ARK Innovation ETF",
        "description": "ARKK is an actively managed ETF that seeks long-term growth of capital by investing under normal circumstances primarily (at least 65% of its assets) in domestic and foreign equity securities of companies that are relevant to the Fund’s investment theme of disruptive innovation.",
        "fund_type": "Active Equity ETF",
        "inception_date": "2014-10-31",
        "cusip": "00214Q104",
        "isin": "US00214Q1040",
        "website": "https://ark-funds.com/arkk"
    }
}
```

## ETF Holdings (v2)

    GET /v2/etf/holdings

Returns ARK ETF holdings

### Query Parameters

| Parameter | Required | Description                 |
| --------- | :------: | --------------------------- |
| symbol    |   YES    | ARK ETF symbol              |
| date_from |    NO    | From date (ISO 8601 format) |
| date_to   |    NO    | To date   (ISO 8601 format) |
| limit     |    NO    | Limit number of results     |

### Example

#### Request

    GET https://arkfunds.io/api/v2/etf/holdings?symbol=ARKK&limit=3

#### Response

``` json
{
    "symbol": "ARKK",
    "date_from": "2021-08-20",
    "date_to": "2021-08-20",
    "holdings": [{
        "date": "2021-08-20",
        "ticker": "TSLA",
        "company": "TESLA INC",
        "cusip": "88160R101",
        "shares": 3256252,
        "market_value": 2192988034.44,
        "weight": 10.56,
        "weight_rank": 1
    }, {
        "date": "2021-08-20",
        "ticker": "TDOC",
        "company": "TELADOC HEALTH INC",
        "cusip": "87918A105",
        "shares": 8555254,
        "market_value": 1160092442.4,
        "weight": 5.59,
        "weight_rank": 2
    }, {
        "date": "2021-08-20",
        "ticker": "ROKU",
        "company": "ROKU INC",
        "cusip": "77543R102",
        "shares": 3269279,
        "market_value": 1122506944.65,
        "weight": 5.4,
        "weight_rank": 3
    }]
}
```

## ETF Trades (v2)

    GET /v2/etf/trades

Returns ARK ETF intraday trades

### Query Parameters

| Parameter | Required | Description                 |
| --------- | :------: | --------------------------- |
| symbol    |   YES    | ARK ETF symbol              |
| date_from |    NO    | From date (ISO 8601 format) |
| date_to   |    NO    | To date   (ISO 8601 format) |
| limit     |    NO    | Limit number of results     |

### Example

#### Request

    GET https://arkfunds.io/api/v2/etf/trades?symbol=ARKK&limit=3

#### Response

``` json
{
    "symbol": "ARKK",
    "date_from": "2021-08-20",
    "date_to": "2021-08-20",
    "trades": [{
        "date": "2021-08-20",
        "ticker": "BEAM",
        "company": "BEAM THERAPEUTICS INC",
        "direction": "Buy",
        "cusip": "07373V105",
        "shares": 5190,
        "etf_percent": 0.0025
    }, {
        "date": "2021-08-20",
        "ticker": "FATE",
        "company": "FATE THERAPEUTICS INC",
        "direction": "Buy",
        "cusip": "31189P102",
        "shares": 292854,
        "etf_percent": 0.0982
    }, {
        "date": "2021-08-20",
        "ticker": "SGFY",
        "company": "SIGNIFY HEALTH INC",
        "direction": "Buy",
        "cusip": "82671G100",
        "shares": 18900,
        "etf_percent": 0.0023
    }]
}
```

## ETF News (v2)

    GET /v2/etf/news

Returns ARK ETF news

### Query Parameters

| Parameter | Required | Description                 |
| --------- | :------: | --------------------------- |
| symbol    |   YES    | ARK ETF symbol              |
| date_from |    NO    | From date (ISO 8601 format) |
| date_to   |    NO    | To date   (ISO 8601 format) |
| limit     |    NO    | Limit number of results     |

### Example

#### Request

    GET https://arkfunds.io/api/v2/etf/news?symbol=ARKG&date_from=2021-04-02&date_to=2021-04-05

#### Response

``` json
{
    "symbol": "ARKG",
    "date_from": "2021-04-02",
    "date_to": "2021-04-05",
    "news": [{
        "id": 41,
        "datetime": "2021-04-05T12:03:00+00:00",
        "related": "ARKG",
        "source": "MarketWatch",
        "headline": "Tesla is on fire, but these EV-related stocks could end up just as hot",
        "summary": "There are many ways to play the electric-vehicle industry as it grows exponentially.",
        "url": "https://www.marketwatch.com/story/tesla-is-on-fire-but-these-ev-related-stocks-could-end-up-just-as-hot-11617638639",
        "image": "https://images.mktw.net/im-320482/social"
    }, {
        "id": 42,
        "datetime": "2021-04-02T07:27:32+00:00",
        "related": "ARKG",
        "source": "seekingalpha.com",
        "headline": "ARK Genomic Revolution Multi-Sector ETF: Poised For Continued Underperformance",
        "summary": "I am neutral on the ETF. For short-term gains, investors may wish to look elsewhere.",
        "url": "https://seekingalpha.com/article/4417325-ark-genomic-revolution-multi-sector-etf-underperformance",
        "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/842211270/medium_image_842211270.jpg"
    }]
}
```

## Stock Profile (v2)

    GET /v2/stock/profile

Returns Stock profile information

### Query Parameters

| Parameter | Required | Description  |
| --------- | :------: | ------------ |
| symbol    |   YES    | Stock symbol |

### Example

#### Request

    GET https://arkfunds.io/api/v2/stock/profile?symbol=TSLA

#### Response

``` json
{
    "symbol": "TSLA",
    "profile": {
        "ticker": "TSLA",
        "name": "Tesla, Inc.",
        "country": "United States",
        "industry": "Auto Manufacturers",
        "sector": "Consumer Cyclical",
        "fullTimeEmployees": 70757,
        "summary": "Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems in the United States, China, and internationally. The company operates in two segments, Automotive, and Energy Generation and Storage. The Automotive segment offers electric vehicles, as well as sells automotive regulatory credits. It provides sedans and sport utility vehicles through direct and used vehicle sales, a network of Tesla Superchargers, and in-app upgrades; and purchase financing and leasing services. This segment is also involved in the provision of non-warranty after-sales vehicle services, sale of used vehicles, retail merchandise, and vehicle insurance, as well as sale of products through its subsidiaries to third party customers; services for electric vehicles through its company-owned service locations, and Tesla mobile service technicians; and vehicle limited warranties and extended service plans. The Energy Generation and Storage segment engages in the design, manufacture, installation, sale, and leasing of solar energy generation and energy storage products, and related services to residential, commercial, and industrial customers and utilities through its website, stores, and galleries, as well as through a network of channel partners. This segment also offers service and repairs to its energy product customers, including under warranty; and various financing options to its solar customers. The company was formerly known as Tesla Motors, Inc. and changed its name to Tesla, Inc. in February 2017. Tesla, Inc. was founded in 2003 and is headquartered in Palo Alto, California.",
        "website": "http://www.tesla.com",
        "market": "us_market",
        "exchange": "NasdaqGS",
        "currency": "USD",
        "marketCap": 673467596800.0,
        "sharesOutstanding": 990014976
    }
}
```

## Stock Trades (v2)

    GET /v2/stock/trades

Returns Stock Trades

### Query Parameters

| Parameter | Required | Description                 |
| --------- | :------: | --------------------------- |
| symbol    |   YES    | Stock symbol                |
| direction |    NO    | Filter on buy/sell          |
| date_from |    NO    | From date (ISO 8601 format) |
| date_to   |    NO    | To date   (ISO 8601 format) |
| limit     |    NO    | Limit number of results     |


### Example

#### Request

    GET https://arkfunds.io/api/v2/stock/trades?symbol=TSLA&date_from=2021-08-01&direction=sell

#### Response

``` json
{
    "symbol": "TSLA",
    "date_from": "2021-08-01",
    "date_to": "2021-08-05",
    "trades": [{
        "date": "2021-08-05",
        "fund": "ARKK",
        "direction": "Sell",
        "shares": 144200,
        "etf_percent": 0.4478
    }, {
        "date": "2021-08-05",
        "fund": "ARKW",
        "direction": "Sell",
        "shares": 19558,
        "etf_percent": 0.2365
    }, {
        "date": "2021-08-04",
        "fund": "ARKW",
        "direction": "Sell",
        "shares": 8100,
        "etf_percent": 0.0989
    }]
}
```

## Stock Fund Ownership (v2)

    GET /v2/stock/fund-ownership

Returns Stock Fund Ownership

### Query Parameters

| Parameter | Required | Description                 |
| --------- | :------: | --------------------------- |
| symbol    |   YES    | Stock symbol                |
| date_from |    NO    | From date (ISO 8601 format) |
| date_to   |    NO    | To date   (ISO 8601 format) |
| limit     |    NO    | Limit number of results     |

### Example

#### Request

    GET https://arkfunds.io/api/v2/stock/fund-ownership?symbol=TSLA

#### Response

``` json
{
    "symbol": "TSLA",
    "date_from": "2021-08-20",
    "date_to": "2021-08-20",
    "data": [{
        "date": "2021-08-20",
        "ownership": [{
            "date": "2021-08-20",
            "fund": "ARKK",
            "weight": 10.56,
            "weight_rank": 1,
            "shares": 3256252,
            "market_value": 2192988034.44
        }, {
            "date": "2021-08-20",
            "fund": "ARKQ",
            "weight": 11.93,
            "weight_rank": 1,
            "shares": 458874,
            "market_value": 309037872.78
        }, {
            "date": "2021-08-20",
            "fund": "ARKW",
            "weight": 10.38,
            "weight_rank": 1,
            "shares": 843781,
            "market_value": 568261190.07
        }],
        "totals": {
            "funds": 3,
            "shares": 4558907,
            "market_value": 3070287097.2900004
        }
    }]
}
```

## ETF Profile (v1)

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

## ETF Holdings (v1)

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

## ETF Trades (v1)

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

## ETF News (v1)

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

## Stock Profile (v1)

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

## Stock Trades (v1)

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

## Stock Fund Ownership (v1)

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