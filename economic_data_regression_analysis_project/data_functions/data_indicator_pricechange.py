import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def calculate_price_change(ticker, start_date, end_date):
    # Convert start_date and end_date to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # Calculate new start date to ensure we have enough data for weekly, monthly, and quarterly price changes
    new_start_date = start_date - timedelta(days=131)

    # Download stock data
    data = yf.download(ticker, start=new_start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    
    # Calculate daily price change
    data['Daily Change'] = data['Close'].diff()
    
    # Calculate weekly price change
    data['Weekly Change'] = data['Close'].diff(7)
    
    # Calculate monthly price change
    data['Monthly Change'] = data['Close'].diff(30)
    
    # Calculate quarterly price change
    data['Quarterly Change'] = data['Close'].diff(90)
    
    # Filter data for the original date range
    data = data.loc[start_date:end_date]
    
    # Select only the date and calculated columns
    data = data[['Daily Change', 'Weekly Change', 'Monthly Change', 'Quarterly Change']]
    
    # Save data to a CSV file
    data.to_csv(f'indicator_{ticker}_price_change.csv')
