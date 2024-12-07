# Import necessary libraries
import yfinance as yf  # For fetching financial data from Yahoo Finance
import streamlit as st  # For building the interactive web app
import pandas as pd  # For handling and analyzing the stock data

# App Title and Description
# win + . to get different empjis

st.write("""
# Simple Stock Price App 📈 

This app displays the **stock closing prices** and **volume** for **Google (Alphabet Inc.)** over a specified timeframe.
""")

# Define the stock ticker symbol
# A ticker symbol is a unique identifier assigned to a publicly traded company's stock
# 'GOOGL' is the ticker symbol for Alphabet Inc. (Google's parent company)
ticker_symbol = 'GOOGL'

# Fetch stock data using yfinance
ticker_data = yf.Ticker(ticker_symbol)  # Create a Ticker object to access stock data

# Retrieve historical stock data
# Set the desired time period for analysis
start_date = '2010-05-21'  # Start date for historical data
end_date = '2020-05-31'  # End date for historical data

# Use the history method to fetch stock data for the specified period
# This returns a Pandas DataFrame with historical stock prices and volume
ticker_df = ticker_data.history(period='1d', start=start_date, end=end_date)

# DataFrame includes:
# Open, High, Low, Close, Volume, Dividends, and Stock Splits

# Display a line chart of the stock's closing price
st.write("### Google Stock Closing Prices Over Time")
# Method 1:
st.line_chart(ticker_df['Close'])  # Visualize the 'Close' column to show price trends
# Method 2:
# st.line_chart(ticker_df.Close)



# Display a line chart of the stock's trading volume
st.write("### Google Stock Trading Volume Over Time")
# Method 1:
st.line_chart(ticker_df['Volume'])  # Visualize the 'Volume' column to show trading activity
# Method 2:
# st.line_chart(ticker_df.Volume)

# Add informative notes about the data
st.write("""
### Notes:
- **Closing Price**: The last price the stock traded for on a particular day.
- **Trading Volume**: The total number of shares traded during a particular day.
""")

st.write("""
### - This app is made by **Ghulam Hussain Khuhro**  
Check out the [GitHub repository](https://github.com/ghulamhussainkhuhro/Streamlit_Apps/tree/main/Simple%20Stock%20Price%20App)  
Connect with me on [LinkedIn](https://www.linkedin.com/in/ghulamhussainkhuhro)
""")

# When we run a streamlit app through terminal by writing Streamlit run app.py then the terminal is dedicated to receive the requests for the app 
# The terminal session becomes "dedicated" to this process and logs server activity (e.g., user interactions, error messages, etc.).

# If you need to regain control of the terminal:
# Press Ctrl + C