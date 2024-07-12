import yfinance as yf
import pandas as pd
from datetime import datetime

def calculate_trading_volume(ticker, start_date, end_date):
    # Download stock data
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Select only the date and Volume columns
    data = data[['Volume']]
    
    # Save data to a CSV file
    data.to_csv(f'indicator_{ticker}_trading_volume.csv')

