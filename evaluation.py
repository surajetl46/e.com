from sklearn.metrics import mean_squared_error
import numpy as np

def calculate_rmse(actual, predicted):
    """
    Calculate the Root Mean Squared Error (RMSE) for the predictions.
    """
    return np.sqrt(mean_squared_error(actual, predicted))

def precision_at_k(recommendations, actual_items, k):
    """
    Calculate Precision@K for the recommendations.
    """
    recommendations = recommendations[:k]
    hits = len(set(recommendations) & set(actual_items))
    return hits / k
