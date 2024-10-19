import pandas as pd

def read_data(file_path):
    """
    Read CRM data from a CSV file.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    DataFrame: A pandas DataFrame containing the CRM data.
    """
    data = pd.read_csv(file_path)
    return data
