import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def calculate_volatility(ticker, start_date, end_date):
    # Convert start_date and end_date to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # Calculate new start date to ensure we have enough data for volatility calculation
    new_start_date = start_date - timedelta(days=365)  # Fetch additional 1 year of data

    # Download stock data
    data = yf.download(ticker, start=new_start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    
    # Calculate daily returns
    data['Return'] = data['Close'].pct_change()
    
    # Calculate volatility
    data['Volatility'] = data['Return'].rolling(window=252).std() * np.sqrt(252)
    
    # Filter data for the original date range
    data = data.loc[start_date:end_date]
    
    # Select only the date and volatility columns
    data = data[['Volatility']]
    
    # Save data to a CSV file
    data.to_csv(f'indicator_{ticker}_volatility.csv')

