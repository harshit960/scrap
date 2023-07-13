import pandas as pd

def read_excel_file(filename):
    # Read the Excel file
    df = pd.read_excel(filename)

    # Create a dictionary to store the lists
    column_lists = {}

    # Iterate over the columns
    for column in df.columns:
        # Get the column data as a list
        column_data = df[column].tolist()
        # Add the list to the dictionary using the column name as the key
        column_lists[column] = column_data

    return column_lists


filename = r"C:\Users\abhi9\OneDrive\Documents\GitHub\scrap\files\input.xlsx"

# Call the function to read the Excel file
result = read_excel_file(filename)

# Print the lists
for column, data in result.items():
    print(f"{column}: {data}")
