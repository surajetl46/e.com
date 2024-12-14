from surprise import SVD, Dataset, Reader

def train_collaborative_filtering(user_item_matrix):
    """
    Train a collaborative filtering model using Surprise.
    """
    reader = Reader(rating_scale=(0, 1))
    interaction_data = Dataset.load_from_df(
        user_item_matrix.reset_index().melt(id_vars='CustomerID', var_name='StockCode', value_name='InteractionValue'),
        reader
    )
    trainset = interaction_data.build_full_trainset()
    model = SVD(n_factors=50, reg_all=0.02, lr_all=0.005)
    model.fit(trainset)
    return model, {}
