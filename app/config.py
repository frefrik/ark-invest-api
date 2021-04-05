# Data update interval (minutes)
UPDATE_INTERVAL_TRADES = 10

# Custom OpenAPI
OPENAPI_TITLE = "ARK Invest API"
OPENAPI_API_VERSION = "1.1.1"
OPENAPI_DESCRIPTION = "API for tracking ARK Invest fund holdings and trades. This site is not affiliated with Ark Invest."
OPENAPI_CONTACT = "api (at) arkfunds.io"
OPENAPI_HOST = "arkfunds.io"
OPENAPI_SERVER_URL = "https://arkfunds.io/api"
OPENAPI_SERVER_BASEPATH = "api"
OPENAPI_EXTERNALDOCS_DESC = "Find out more about this project"
OPENAPI_EXTERNALDOCS_URL = "https://github.com/frefrik/ark-invest-api"

# ARK settings
FUNDS = ["ARKK", "ARKQ", "ARKW", "ARKG", "ARKF", "ARKX", "PRNT", "IZRL"]

BASE_URL_HOLDINGS = "https://ark-funds.com/wp-content/fundsiteliterature/csv/"
BASE_URL_TRADES = "https://ark-funds.com/auto/trades/"
TRADE_STATUS_URL = "https://ark-funds.com/auto/getidt.php"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:86.0) Gecko/20100101 Firefox/86.0",
}

FUND_HOLDINGS_FILES = {
    "ARKK": "ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv",
    "ARKQ": "ARK_AUTONOMOUS_TECHNOLOGY_&_ROBOTICS_ETF_ARKQ_HOLDINGS.csv",
    "ARKW": "ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv",
    "ARKG": "ARK_GENOMIC_REVOLUTION_MULTISECTOR_ETF_ARKG_HOLDINGS.csv",
    "ARKF": "ARK_FINTECH_INNOVATION_ETF_ARKF_HOLDINGS.csv",
    "ARKX": "ARK_SPACE_EXPLORATION_&_INNOVATION_ETF_ARKX_HOLDINGS.csv",
    "PRNT": "THE_3D_PRINTING_ETF_PRNT_HOLDINGS.csv",
    "IZRL": "ARK_ISRAEL_INNOVATIVE_TECHNOLOGY_ETF_IZRL_HOLDINGS.csv",
}

# Example json output
HOLDINGS_FUND_EXAMPLE = {
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
}

TRADES_FUND_EXAMPLE = {
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
}

FUNDS_EXAMPLE = {
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

STOCK_PROFILE_EXAMPLE = {
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
}

FUND_OWNERSHIP_EXAMPLE = {
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
}

STOCK_TRADES_EXAMPLE = {
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
}
