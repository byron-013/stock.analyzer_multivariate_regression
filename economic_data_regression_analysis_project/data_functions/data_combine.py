import pandas as pd

def merge_csv_files(file_list, output_file):
    # Initialize an empty DataFrame
    merged_data = pd.DataFrame()

    # Loop through the list of files
    for file in file_list:
        # Read the CSV file
        data = pd.read_csv(file)
        
        # If merged_data is empty, copy data
        if merged_data.empty:
            merged_data = data
        else:
            # Merge data with merged_data
            merged_data = pd.merge(merged_data, data, on='Date')

    # Save the merged data to a new CSV file
    merged_data.to_csv(output_file, index=False)

# Example usage:
# merge_csv_files(['file1.csv', 'file2.csv', 'file3.csv'], 'merged_data.csv')
