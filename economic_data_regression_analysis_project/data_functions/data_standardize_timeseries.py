import pandas as pd
import numpy as np

def standardize_data(csv_file, frequency, fill_method):
    # Read CSV file
    df = pd.read_csv(csv_file, parse_dates=['Date'], index_col='Date')
    
    # Determine start and end dates from the data
    start_date = df.index.min()
    end_date = df.index.max()

    # Create a new DataFrame that includes all calendar days in the given range
    all_dates = pd.date_range(start=start_date, end=end_date)
    df_all_dates = pd.DataFrame(index=all_dates)
    
    # Join the original DataFrame with the new DataFrame
    df = df_all_dates.join(df)
    
    # Resample data based on the provided frequency
    if frequency == 'daily':
        df = df.resample('D').mean()
    elif frequency == 'weekly':
        df = df.resample('W').mean()
    elif frequency == 'monthly':
        df = df.resample('M').mean()
    else:
        print(f'Unknown frequency: {frequency}')
        return

    # Handle missing values based on the provided method
    if fill_method == 'fill_0':
        df = df.fillna(0)
    elif fill_method == 'fill_avg':
        df = df.fillna(df.mean())
    elif fill_method == 'fill_NaN':
        df = df.fillna(np.nan)
    elif fill_method == 'dont_fill':
        pass
    else:
        print(f'Unknown fill method: {fill_method}')
        return

    # Give a name to the index
    df.index.name = 'Date'

    # Save the DataFrame to a new CSV file

    output_file = f'standardized_{csv_file}'
    df.to_csv(output_file)
    return output_file


