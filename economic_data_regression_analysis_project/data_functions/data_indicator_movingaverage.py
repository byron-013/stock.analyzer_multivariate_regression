import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def calculate_moving_averages(ticker, start_date, end_date):
    # Convert start_date and end_date to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # Calculate new start date to ensure we have enough data for moving average calculation
    new_start_date = start_date - timedelta(days=300) 

    # Download stock data
    data = yf.download(ticker, start=new_start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    
    # Calculate moving averages
    for window in [15, 20, 30, 50, 100, 200]:
        data[f'{window}D MA'] = data['Close'].rolling(window=window).mean()
    
    # Filter data for the original date range
    data = data.loc[start_date:end_date]
    
    # Select only the date and moving average columns
    data = data[[f'{window}D MA' for window in [15, 20, 30, 50, 100, 200]]]
    # Save data to a CSV file
    data.to_csv(f'indicator_{ticker}_moving_averages.csv')



