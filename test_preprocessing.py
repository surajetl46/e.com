import unittest
from data_preprocessing import preprocess_data
import pandas as pd

class TestPreprocessing(unittest.TestCase):
    def test_preprocess_data(self):
        mock_data = pd.DataFrame({
            'CustomerID': ['1', '2', '1', '3'],
            'StockCode': ['A', 'A', 'B', 'C'],
            'Quantity': [1, 1, 1, 1]
        })
        result = preprocess_data(mock_data)
        self.assertTrue('A' in result.columns)
        self.assertTrue('1' in result.index)

if __name__ == '__main__':
    unittest.main()
