# OpenAPI settings
OPENAPI_TITLE = "ARK Invest API"
OPENAPI_API_VERSION = "2.4.4"
OPENAPI_DESCRIPTION = "API for tracking ARK Invest fund holdings and trades. This site is not affiliated with Ark Invest."
OPENAPI_CONTACT = "api@arkfunds.io"
OPENAPI_SERVER_URL = "https://arkfunds.io/api"
OPENAPI_EXTERNALDOCS_DESC = "Find out more about this project"
OPENAPI_EXTERNALDOCS_URL = "https://github.com/frefrik/ark-invest-api"

# ARK settings
FUNDS = [
    "ARKA",
    "ARKB",
    "ARKC",
    "ARKD",
    "ARKZ",
    "ARKY",
    "ARKK",
    "ARKQ",
    "ARKW",
    "ARKG",
    "ARKF",
    "ARKX",
    "ARKVX",
    "PRNT",
    "IZRL",
    "CTRU",
]

# Example responses
RESPONSES = {
    "v1": {
        "etf_profile": {
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
        },
        "etf_holdings": {
            "symbol": "ARKK",
            "date": "2021-01-06",
            "holdings": [
                {
                    "company": "TESLA INC",
                    "ticker": "TSLA",
                    "cusip": "88160R101",
                    "shares": 2710821,
                    "market_value": 2049326459.58,
                    "weight": 10.99,
                    "weight_rank": 1,
                },
                {
                    "company": "ROKU INC",
                    "ticker": "ROKU",
                    "cusip": "77543R102",
                    "shares": 3774458,
                    "market_value": 1294450371.1,
                    "weight": 6.94,
                    "weight_rank": 2,
                },
                {
                    "company": "CRISPR THERAPEUTICS AG",
                    "ticker": "CRSP",
                    "cusip": "H17182108",
                    "shares": 6384590,
                    "market_value": 1046115071.5,
                    "weight": 5.61,
                    "weight_rank": 3,
                },
                {
                    "company": "SQUARE INC - A",
                    "ticker": "SQ",
                    "cusip": "852234103",
                    "shares": 4385414,
                    "market_value": 995006582.46,
                    "weight": 5.34,
                    "weight_rank": 4,
                },
                {
                    "company": "TELADOC HEALTH INC",
                    "ticker": "TDOC",
                    "cusip": "87918A105",
                    "shares": 3971375,
                    "market_value": 810756206.25,
                    "weight": 4.35,
                    "weight_rank": 5,
                },
            ],
        },
        "etf_trades": {
            "symbol": "ARKK",
            "date_from": "2021-01-14",
            "date_to": "2021-01-14",
            "trades": [
                {
                    "fund": "ARKK",
                    "date": "2021-01-14",
                    "direction": "Buy",
                    "ticker": "TXG",
                    "cusip": "88025U109",
                    "company": "10X GENOMICS INC",
                    "shares": 125794,
                    "etf_percent": 0.1,
                },
                {
                    "fund": "ARKK",
                    "date": "2021-01-14",
                    "direction": "Buy",
                    "ticker": "REGN",
                    "cusip": "75886F107",
                    "company": "REGENERON PHARMACEUTICALS INC",
                    "shares": 36509,
                    "etf_percent": 0.08,
                },
            ],
        },
        "etf_news": {
            "symbol": "ARKX",
            "date_from": "2021-04-07",
            "date_to": "2021-04-08",
            "news": [
                {
                    "id": 2,
                    "datetime": "2021-04-08T18:40:16+00:00",
                    "related": "ARKX",
                    "source": "seekingalpha.com",
                    "headline": "Nicholas Ward's Dividend Growth Portfolio March 2021 Review",
                    "summary": "March 2021 was my best dividend income month yet. My passive income was up 13.6% y/y during March. My portfolio's total return during March was 3.47%.",
                    "url": "https://seekingalpha.com/article/4418244-nicholas-ward-dividend-growth-portfolio-march-2021-review",
                    "image": "https://static.seekingalpha.com/uploads/2021/4/4/50407678-16175234983922832_origin.png",
                },
                {
                    "id": 3,
                    "datetime": "2021-04-08T11:17:00+00:00",
                    "related": "ARKX",
                    "source": "DowJones",
                    "headline": "Global COVID-19 cases top 133 million as Brazil and India become flashpoints",
                    "summary": "The number of global confirmed cases of the coronavirus-borne illness COVID-19 climbed above 133 million on Thursday and the death toll edged closer to 3...",
                    "url": "https://www.marketwatch.com/story/global-covid-19-cases-top-133-million-as-brazil-and-india-become-flashpoints-11617895045",
                    "image": "https://images.mktw.net/im-322270/social",
                },
                {
                    "id": 4,
                    "datetime": "2021-04-08T08:52:00+00:00",
                    "related": "ARKX",
                    "source": "DowJones",
                    "headline": "G-20 nearer to a deal on minimum corporate tax rate",
                    "summary": "Finance ministers from the world’s most developed economies said on Wednesday they hoped to agree on an overhaul of the way multinationals are taxed as well...",
                    "url": "https://www.marketwatch.com/story/g-20-nearer-to-a-deal-on-minimum-corporate-tax-rate-11617886359",
                    "image": "https://images.mktw.net/im-322159/social",
                },
                {
                    "id": 5,
                    "datetime": "2021-04-07T23:39:00+00:00",
                    "related": "ARKX",
                    "source": "Benzinga",
                    "headline": "Cathie Wood Adds These Stocks To The Newly-Created Space Exploration ETF And Others",
                    "summary": "Cathie Wood’s Ark Investment Management sends out an email every night listing the stocks that were bought or sold by the firm's ETFs that day. In recent months, the...",
                    "url": "https://www.benzinga.com/news/21/04/20532249/cathie-wood-adds-these-stocks-to-the-newly-created-space-exploration-etf-and-others",
                    "image": "https://cdn.benzinga.com/files/imagecache/og_image_social_share_1200x630/images/story/2012/micheile-henderson-lz_4npfkcv8-unsplash_1_5.jpg",
                },
            ],
        },
        "stock_profile": {
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
            "marketCap": 783117844480.0,
            "sharesOutstanding": 947900992,
        },
        "stock_trades": {
            "symbol": "TSLA",
            "date_from": "2020-09-18",
            "date_to": "2021-01-12",
            "trades": [
                {
                    "date": "2021-01-12",
                    "fund": "ARKK",
                    "direction": "Sell",
                    "ticker": "TSLA",
                    "company": "TESLA INC",
                    "cusip": "88160R101",
                    "shares": 126276,
                    "etf_percent": 0.5055,
                },
                {
                    "date": "2021-01-12",
                    "fund": "ARKQ",
                    "direction": "Sell",
                    "ticker": "TSLA",
                    "company": "TESLA INC",
                    "cusip": "88160R101",
                    "shares": 13179,
                    "etf_percent": 0.4991,
                },
                {
                    "date": "2021-01-12",
                    "fund": "ARKW",
                    "direction": "Sell",
                    "ticker": "TSLA",
                    "company": "TESLA INC",
                    "cusip": "88160R101",
                    "shares": 16898,
                    "etf_percent": 0.6161,
                },
                {
                    "date": "2021-01-08",
                    "fund": "ARKK",
                    "direction": "Sell",
                    "ticker": "TSLA",
                    "company": "TESLA INC",
                    "cusip": "88160R101",
                    "shares": 59500,
                    "etf_percent": 0.2506,
                },
            ],
        },
        "stock_fund_ownership": {
            "symbol": "TDOC",
            "date": "2021-01-15",
            "ownership": [
                {
                    "fund": "ARKK",
                    "weight": 4.33,
                    "weight_rank": 5,
                    "shares": 4325169,
                    "market_value": 974244317.25,
                },
                {
                    "fund": "ARKW",
                    "weight": 3.73,
                    "weight_rank": 5,
                    "shares": 1017599,
                    "market_value": 229214174.75,
                },
                {
                    "fund": "ARKG",
                    "weight": 6.4,
                    "weight_rank": 2,
                    "shares": 2978073,
                    "market_value": 670810943.25,
                },
                {
                    "fund": "ARKF",
                    "weight": 1.35,
                    "weight_rank": 31,
                    "shares": 143362,
                    "market_value": 32292290.5,
                },
            ],
        },
    },
    "v2": {
        "etf_profile": {
            "symbol": "ARKK",
            "profile": {
                "symbol": "ARKK",
                "name": "ARK Innovation ETF",
                "description": "ARKK is an actively managed ETF that seeks long-term growth of capital by investing under normal circumstances primarily (at least 65% of its assets) in domestic and foreign equity securities of companies that are relevant to the Fund’s investment theme of disruptive innovation.",
                "fund_type": "Active Equity ETF",
                "inception_date": "2014-10-31",
                "cusip": "00214Q104",
                "isin": "US00214Q1040",
                "website": "https://ark-funds.com/arkk",
            },
        },
        "etf_holdings": {
            "symbol": "ARKK",
            "date_from": "2021-10-08",
            "date_to": "2021-10-08",
            "holdings": [
                {
                    "fund": "ARKK",
                    "date": "2021-10-08",
                    "ticker": "TSLA",
                    "company": "TESLA INC",
                    "cusip": "88160R101",
                    "shares": 2469443,
                    "market_value": 1959774659.23,
                    "share_price": 793.61,
                    "weight": 9.65,
                    "weight_rank": 1,
                },
                {
                    "fund": "ARKK",
                    "date": "2021-10-08",
                    "ticker": "TDOC",
                    "company": "TELADOC HEALTH INC",
                    "cusip": "87918A105",
                    "shares": 9124177,
                    "market_value": 1193442351.6,
                    "share_price": 130.8,
                    "weight": 5.88,
                    "weight_rank": 2,
                },
                {
                    "fund": "ARKK",
                    "date": "2021-10-08",
                    "ticker": "ROKU",
                    "company": "ROKU INC",
                    "cusip": "77543R102",
                    "shares": 3561738,
                    "market_value": 1155677128.86,
                    "share_price": 324.47,
                    "weight": 5.69,
                    "weight_rank": 3,
                },
            ],
        },
        "etf_trades": {
            "symbol": "ARKK",
            "date_from": "2021-10-08",
            "date_to": "2021-10-08",
            "trades": [
                {
                    "fund": "ARKK",
                    "date": "2021-10-08",
                    "ticker": "NTLA",
                    "company": "INTELLIA THERAPEUTICS INC",
                    "direction": "Buy",
                    "cusip": "45826J105",
                    "shares": 269179,
                    "etf_percent": 0.1608,
                },
                {
                    "fund": "ARKK",
                    "date": "2021-10-08",
                    "ticker": "CRSP",
                    "company": "CRISPR THERAPEUTICS AG",
                    "direction": "Buy",
                    "cusip": "H17182108",
                    "shares": 268472,
                    "etf_percent": 0.1293,
                },
                {
                    "fund": "ARKK",
                    "date": "2021-10-08",
                    "ticker": "DOCU",
                    "company": "DOCUSIGN INC",
                    "direction": "Sell",
                    "cusip": "256163106",
                    "shares": 78867,
                    "etf_percent": 0.103,
                },
            ],
        },
        "etf_news": {
            "symbol": "ARKG",
            "date_from": "2021-04-02",
            "date_to": "2021-04-05",
            "news": [
                {
                    "id": 41,
                    "datetime": "2021-04-05T12:03:00+00:00",
                    "related": "ARKG",
                    "source": "MarketWatch",
                    "headline": "Tesla is on fire, but these EV-related stocks could end up just as hot",
                    "summary": "There are many ways to play the electric-vehicle industry as it grows exponentially.",
                    "url": "https://www.marketwatch.com/story/tesla-is-on-fire-but-these-ev-related-stocks-could-end-up-just-as-hot-11617638639",
                    "image": "https://images.mktw.net/im-320482/social",
                },
                {
                    "id": 42,
                    "datetime": "2021-04-02T07:27:32+00:00",
                    "related": "ARKG",
                    "source": "seekingalpha.com",
                    "headline": "ARK Genomic Revolution Multi-Sector ETF: Poised For Continued Underperformance",
                    "summary": "I am neutral on the ETF. For short-term gains, investors may wish to look elsewhere.",
                    "url": "https://seekingalpha.com/article/4417325-ark-genomic-revolution-multi-sector-etf-underperformance",
                    "image": "https://static.seekingalpha.com/cdn/s3/uploads/getty_images/842211270/medium_image_842211270.jpg",
                },
            ],
        },
        "etf_performance": {
            "symbol": "ARKK",
            "performance": [
                {
                    "fund": "ARKK",
                    "overview": {
                        "asOfDate": "2022-06-24",
                        "ytdReturn": "-53.52%",
                        "oneYearReturn": "-64.10%",
                        "threeYearReturn": "-0.03%",
                    },
                    "trailingReturns": {
                        "asOfDate": "2022-06-16",
                        "ytd": "-60.84%",
                        "oneMonth": "-9.81%",
                        "threeMonth": "-38.15%",
                        "oneYear": "-67.38%",
                        "threeYear": "-3.90%",
                        "fiveYear": "12.68%",
                        "tenYear": "0.00%",
                    },
                    "annualReturns": [
                        {
                            "year": "2022",
                            "value": "",
                        },
                        {
                            "year": "2021",
                            "value": "-23.35%",
                        },
                        {
                            "year": "2020",
                            "value": "156.61%",
                        },
                        {
                            "year": "2019",
                            "value": "35.73%",
                        },
                        {
                            "year": "2018",
                            "value": "3.58%",
                        },
                        {
                            "year": "2017",
                            "value": "87.38%",
                        },
                        {
                            "year": "2016",
                            "value": "-1.96%",
                        },
                        {
                            "year": "2015",
                            "value": "3.76%",
                        },
                    ],
                }
            ],
        },
        "stock_profile": {
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
                "sharesOutstanding": 990014976,
            },
        },
        "stock_trades": {
            "symbol": "TSLA",
            "date_from": "2021-08-01",
            "date_to": "2021-08-05",
            "trades": [
                {
                    "date": "2021-08-05",
                    "fund": "ARKK",
                    "direction": "Sell",
                    "shares": 144200,
                    "etf_percent": 0.4478,
                },
                {
                    "date": "2021-08-05",
                    "fund": "ARKW",
                    "direction": "Sell",
                    "shares": 19558,
                    "etf_percent": 0.2365,
                },
                {
                    "date": "2021-08-04",
                    "fund": "ARKW",
                    "direction": "Sell",
                    "shares": 8100,
                    "etf_percent": 0.0989,
                },
            ],
        },
        "stock_fund_ownership": {
            "symbol": "TSLA",
            "date_from": "2021-08-20",
            "date_to": "2021-08-20",
            "data": [
                {
                    "date": "2021-08-20",
                    "ownership": [
                        {
                            "date": "2021-08-20",
                            "fund": "ARKK",
                            "weight": 10.56,
                            "weight_rank": 1,
                            "shares": 3256252,
                            "market_value": 2192988034.44,
                        },
                        {
                            "date": "2021-08-20",
                            "fund": "ARKQ",
                            "weight": 11.93,
                            "weight_rank": 1,
                            "shares": 458874,
                            "market_value": 309037872.78,
                        },
                        {
                            "date": "2021-08-20",
                            "fund": "ARKW",
                            "weight": 10.38,
                            "weight_rank": 1,
                            "shares": 843781,
                            "market_value": 568261190.07,
                        },
                    ],
                    "totals": {
                        "funds": 3,
                        "shares": 4558907,
                        "market_value": 3070287097.2900004,
                    },
                }
            ],
        },
        "stock_price": {
            "symbol": "TSLA",
            "exchange": "NasdaqGS",
            "currency": "USD",
            "price": 793.61,
            "change": 10.859985,
            "changep": 1.3874142,
            "last_trade": "2021-10-07T20:00:02",
        },
    },
}
