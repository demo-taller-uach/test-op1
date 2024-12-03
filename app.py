import streamlit as st
import requests
import pandas as pd

# Function to fetch market prices from a public API
def get_market_prices():
    # API endpoints for market prices (replace with actual API endpoints)
    api_urls = {
        'Gold': 'https://api.example.com/gold',
        'Natural Gas': 'https://api.example.com/natural_gas',
        'S&P 500': 'https://api.example.com/sp500',
        'Bitcoin': 'https://api.example.com/bitcoin'
    }

    prices = {}
    for asset, url in api_urls.items():
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            prices[asset] = data['price']
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
