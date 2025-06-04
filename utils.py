import requests
import pandas as pd
import os
from io import StringIO

def eo_grabber(url: str) -> None:
    """
    Fetches executive order data in CSV format from the provided URL.
    If 'federal_register_data.csv' already exists, appends only new records.

    Parameters:
        url (str): The URL to fetch the executive order data from.

    Returns:
        None
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses

        # Corrected: use StringIO from the io module
        new_df = pd.read_csv(StringIO(response.text))

        file_path = 'federal_register_data.csv'

        if os.path.exists(file_path):
            existing_df = pd.read_csv(file_path)
            combined_df = pd.concat([existing_df, new_df]).drop_duplicates()
        else:
            combined_df = new_df

        combined_df.to_csv(file_path, index=False)
        print(f"Data successfully written to {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
