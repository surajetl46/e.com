from data_preprocessing import load_data, preprocess_data
from model_training import train_collaborative_filtering

def main():
    # Load and preprocess data
    data = load_data('Dataset.csv')
    user_item_matrix = preprocess_data(data)

    # Train the collaborative filtering model
    model, predictions = train_collaborative_filtering(user_item_matrix)
    print("Model training complete.")

if __name__ == '__main__':
    main()
