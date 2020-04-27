IEX_API_KEY = "ddc8d9c2ba3a8008b2099dc5312740ab"

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

