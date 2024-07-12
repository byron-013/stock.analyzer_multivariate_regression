import yfinance as yf
import pandas as pd

def download_stock_data(ticker, start_date, end_date):
    # Download stock data
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Save data to a CSV file
    data.to_csv(f'{ticker}_data.csv')

