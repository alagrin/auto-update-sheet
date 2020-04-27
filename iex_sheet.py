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

# Create an empty pandas DataFrame to append our parsed values into during our for loop
output_data = pd.DataFrame(pd.np.empty((0, 4)))

for ticker in raw_data.columns:

    # Parse the company's name
    company_name = raw_data[ticker]['stats']['companyName']

    # Parse the company's stock price
    stock_price = raw_data[ticker]['price']

    # Parse the company's dividend yield
    dividend_yield = raw_data[ticker]['stats']['dividendYield']

    new_column = pd.Series([ticker, company_name, stock_price, dividend_yield])
    output_data = output_data.append(new_column, ignore_index=True)

# Change the column names of output_data
output_data.columns = ['Ticker', 'Company Name',
                       'Stock Price', 'Dividend Yield']

# Change the index of output_data
output_data.set_index('Ticker', inplace=True)

# Replace the missing values of the 'Dividend Yield' column with 0
output_data['Dividend Yield'].fillna(0, inplace=True)

# Print the DataFrame
output_data
