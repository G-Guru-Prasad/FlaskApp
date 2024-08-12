from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# In-memory storage to simulate data storage
data_storage = {}

# Simulated external service data (mock data)
MOCK_DATA = {
    "product_id": "12345",
    "product_name": "Sample Product",
    "price": 99.99,
    "quantity": 10,
}

# Endpoint to fetch data
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    # Simulate fetching data from an external service
    return jsonify(MOCK_DATA)

# Data processing function
def process_data(data):
    # Example transformation: converting all text values to uppercase
    processed_data = {k: (v.upper() if isinstance(v, str) else v) for k, v in data.items()}
    return processed_data

# Endpoint to process and store data
@app.route('/process-data', methods=['POST'])
def process_and_store_data():
    global data_storage
    # Get data (simulating the retrieval from /fetch-data)
    data = MOCK_DATA
    
    # Process the data
    processed_data = process_data(data)
    
    # Store the processed data in memory
    data_storage = processed_data
    
    return jsonify({"message": "Data processed and stored successfully"}), 200

# Endpoint to retrieve the processed data
@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    if not data_storage:
        return jsonify({"message": "No processed data available"}), 404
    return jsonify(data_storage), 200

if __name__ == '__main__':
    app.run(debug=True)
