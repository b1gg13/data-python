import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown Are the stock closing price and volume of Google!

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')
# Open High Low Close Volume Dividends Stock Split

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)