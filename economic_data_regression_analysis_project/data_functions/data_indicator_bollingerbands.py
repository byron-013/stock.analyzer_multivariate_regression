import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def calculate_bollinger_bands(ticker, start_date, end_date):
    # Convert start_date and end_date to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # Calculate new start date to ensure we have enough data for Bollinger Bands calculation
    new_start_date = start_date - timedelta(days=30) 
    # Download stock data
    data = yf.download(ticker, start=new_start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    
    # Calculate moving average and standard deviation
    data['MA'] = data['Close'].rolling(window=20).mean()
    data['STD'] = data['Close'].rolling(window=20).std()
    
    # Calculate Bollinger Bands
    data['Upper Band'] = data['MA'] + (data['STD'] * 2)
    data['Lower Band'] = data['MA'] - (data['STD'] * 2)
    
    # Filter data for the original date range
    data = data.loc[start_date:end_date]
    
    # Select only the date and Bollinger Bands columns
    data = data[['Upper Band', 'Lower Band']]
    
    # Save data to a CSV file
    data.to_csv(f'indicator_{ticker}_bollinger_bands.csv')
