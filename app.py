import streamlit as st
import requests
import pandas as pd

# Function to fetch market prices from a public API
def get_market_prices():
    # API endpoints for market prices (replace with actual API endpoints)
    api_urls = {
        'Gold':'https://api.commoditypriceapi.com/latest?apikey=YOUR_API_KEY&symbols=XAU'
        'Natural Gas':https://api.commoditypriceapi.com/latest?apikey=YOUR_API_KEY&symbols=NG'https://api.commoditypriceapi.com/latest?apikey=YOUR_API_KEY&symbols=NG'
        'S&P 500': https://api.polygon.io/v1/open-close/stock/SPY?adjusted=true&apiKey=YOUR_API_KEY,
        'Bitcoin': https://api.coindesk.com/v1/bpi/currentprice/BTC.json
    }

    prices = {}
    for asset, url in api_urls.items():
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
    if asset == 'Gold' or asset == 'Natural Gas':
            prices[asset] = data['rates'][0]['price']
        elif asset == 'S&P 500':
            prices[asset] = data['close']
        elif asset == 'Bitcoin':
            prices[asset] = data['bpi']['USD']['rate_float']
        else:
            prices[asset] = 'N/A'
    return prices

# Streamlit app function
def main():
    st.title("Market Prices Dashboard")
    st.write("This dashboard shows the latest market prices for Gold, Natural Gas, S&P 500, and Bitcoin.")

    # Fetch market prices
    prices = get_market_prices()

    # Display market prices in a table
    df = pd.DataFrame(list(prices.items()), columns=['Asset', 'Price'])
    st.table(df)

if __name__ == "__main__":
    main()
