IEX_API_key = "ddc8d9c2ba3a8008b2099dc5312740ab"

import pandas as pd

# Tickers for the 10 largest US companies
tickers = [
    'MSFT',
    'AAPL',
    'AMZN',
    'GOOG',
    'FB',
    'BRK.B',
    'JNJ',
    'WMT',
    'V',
    'PG'
]

# Need a batch call to the API: return JSON w/ few HTTP requests

HTTP_request = "https://cloud.iexapis.com/stable/stock/market/batch?symbols=TICKERS&types=ENDPOINTS&range=RANGE&token=IEX_API_Key"

# ticker string is empty and we add tickers to it
ticker_string = ""

for ticker in tickers:
    ticker_string += ticker
    ticker_string += ","

ticker_string = ticker_string[:-1]

endpoints = 'price,stats'

# interpolating the value into the URL
HTTP_request = f'https://cloud.iexapis.com/stable/stock/market/batch?symbols={ticker_string}&types={endpoints}&range=1y&token={IEX_API_key}'

raw_data = pd.read_json(HTTP_request)
