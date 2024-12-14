from model_training import train_collaborative_filtering
from scipy.spatial.distance import cosine

def get_recommendations(customer_id, user_item_matrix):
    """
    Generate recommendations for a given customer using a hybrid approach.
    """
    # Train collaborative filtering model
    model, predictions = train_collaborative_filtering(user_item_matrix)

    # Content-based filtering (Cosine Similarity)
    customer_vector = user_item_matrix.loc[customer_id].values
    similarities = user_item_matrix.apply(lambda row: 1 - cosine(customer_vector, row.values), axis=1)

    # Combine predictions from CF and CBF
    combined_scores = predictions.get(customer_id, {}) + similarities
    return combined_scores.sort_values(ascending=False).index[:5].tolist()
