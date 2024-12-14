import unittest
from model_training import train_collaborative_filtering
import pandas as pd

class TestModelTraining(unittest.TestCase):
    def test_train_model(self):
        mock_data = pd.DataFrame({
            'CustomerID': ['1', '2', '1', '3'],
            'StockCode': ['A', 'A', 'B', 'C'],
            'Quantity': [1, 1, 1, 1]
        }).pivot_table(
            index='CustomerID', columns='StockCode', values='Quantity', aggfunc='sum', fill_value=0
        )
        model, predictions = train_collaborative_filtering(mock_data)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
