import csv

# Create empty dictionaries for each stock
AAPL_prices = {}
GOOG_prices = {}
MSFT_prices = {}

# Open the CSV file and read in the data
with open('stock_prices.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Extract the stock symbol, date, and price from the row
        symbol = row['Symbol']
        date = row['Date']
        price = float(row['Price'])
        
        # Add the price to the appropriate dictionary
        if symbol == 'AAPL':
            if date in AAPL_prices:
                if price > AAPL_prices[date]['high']:
                    AAPL_prices[date]['high'] = price
                if price < AAPL_prices[date]['low']:
                    AAPL_prices[date]['low'] = price
            else:
                AAPL_prices[date] = {'high': price, 'low': price}
        elif symbol == 'GOOG':
            if date in GOOG_prices:
                if price > GOOG_prices[date]['high']:
                    GOOG_prices[date]['high'] = price
                if price < GOOG_prices[date]['low']:
                    GOOG_prices[date]['low'] = price
            else:
                GOOG_prices[date] = {'high': price, 'low': price}
        elif symbol == 'MSFT':
            if date in MSFT_prices:
                if price > MSFT_prices[date]['high']:
                    MSFT_prices[date]['high'] = price
                if price < MSFT_prices[date]['low']:
                    MSFT_prices[date]['low'] = price
            else:
                MSFT_prices[date] = {'high': price, 'low': price}

# Print out the results
print('AAPL prices:')
for date, prices in AAPL_prices.items():
    print(date, 'high:', prices['high'], 'low:', prices['low'])
print('GOOG prices:')
for date, prices in GOOG_prices.items():
    print(date, 'high:', prices['high'], 'low:', prices['low'])
print('MSFT prices:')
for date, prices in MSFT_prices.items():
    print(date, 'high:', prices['high'], 'low:', prices['low']))
