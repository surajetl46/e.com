import pandas as pd

def load_data(file_path):
    """
    Load the dataset from a CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully. Columns:", data.columns)
        return data
    except Exception as e:
        raise ValueError(f"Error loading data from {file_path}: {e}")

def preprocess_data(data):
    """
    Preprocess the dataset to create a user-item interaction matrix.
    """
    data = data.dropna(subset=['CustomerID', 'StockCode'])
    data['CustomerID'] = data['CustomerID'].astype(str)

    user_item_matrix = pd.pivot_table(
        data,
        index='CustomerID',
        columns='StockCode',
        values='Quantity',
        aggfunc='sum',
        fill_value=0
    )
    return user_item_matrix
