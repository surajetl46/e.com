from flask import Flask, jsonify, request
from data_preprocessing import load_data, preprocess_data
from hybrid_recommendation import get_recommendations

app = Flask(__name__)

# Load and preprocess data
data = load_data('Dataset.csv')
user_item_matrix = preprocess_data(data)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Recommendation System API!"})

@app.route('/recommend', methods=['GET'])
def recommend():
    customer_id = request.args.get('customer_id')
    if not customer_id:
        return jsonify({"error": "Please provide a customer_id parameter"}), 400

    # Generate recommendations for the customer
    recommendations = get_recommendations(customer_id, user_item_matrix)
    if not recommendations:
        return jsonify({"error": f"No recommendations available for customer {customer_id}"}), 404

    return jsonify({"customer_id": customer_id, "recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
