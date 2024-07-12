import pandas as pd

#Function to retrieve data from CSV files given a date range
#MUST HAVE INDEX COLUMN AS THE DATE

def get_economic_data(csv_file, start_date, end_date):
    df = pd.read_csv(csv_file, parse_dates=['Date'], index_col='Date')

    # Filter the data based on the date range
    df_filtered = df.loc[start_date:end_date]

    # Write the filtered data to a new CSV file
    df_filtered.to_csv(f'selected_{csv_file}')