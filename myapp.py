import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price app

Shown are the stock closing **price** and **volume** of META from 2019-5-24 to 2022-9-31  
""")


# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df
# define the ticker symbol
ticker_symbol = 'META'
#get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)
# get the historical prices for this ticker
ticker_df = ticker_data.history(period='id', start='2019-5-24', end='2022-9-31')
# Open      High     Low Close    Volume    Dividends    Stack     splits

st.write("""
## Closing price
""")
st.line_chart(ticker_df.Close)
st.write("""
## Volume Price
""")
st.line_chart(ticker_df.Volume)
