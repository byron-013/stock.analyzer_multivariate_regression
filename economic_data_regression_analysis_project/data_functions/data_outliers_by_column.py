import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def handle_outliers(csv_file, column_indices, method):
    # Read CSV file
    df = pd.read_csv(csv_file)
    
    # Convert column indices to column names
    columns = df.columns[column_indices]

    # Loop through each column
    for column in columns:
        # Calculate the IQR of the column
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1

        # Define the outlier range
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Identify outliers
        outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

        # Handle outliers based on the provided method
        if method == 'fill_0':
            df[column] = df[column].where(~df[column].isin(outliers), 0)
        elif method == 'fill_avg':
            avg = df[column].mean()
            df[column] = df[column].where(~df[column].isin(outliers), avg)
        elif method == 'fill_NaN':
            df[column] = df[column].where(~df[column].isin(outliers), np.nan)
        elif method == 'dont_fill':
            pass
        else:
            print(f'Unknown method: {method}')
            return

    # Save the DataFrame to a new CSV file
    df.to_csv('data_handled_outliers.csv', index=False)

