
from flask import Flask, jsonify, request
import requests

application = Flask(__name__)

# Use the hardcoded Amplify URL directly in the code
AMPLIFY_URL = "https://amplify-webapp-dev-7e83a-deployment.s3.ap-south-1.amazonaws.com/items.json"

# Default route to fetch all items and show them on /
@application.route('/', methods=['GET'])
@application.route('/items', methods=['GET'])
def get_items():
    response = requests.get(AMPLIFY_URL)
    return jsonify(response.json())

# Endpoint to fetch a specific item by id
@application.route('/items/<int:id>', methods=['GET'])
def get_item_by_id(id):
    response = requests.get(AMPLIFY_URL)
    items = response.json()
    item = next((item for item in items if item['id'] == id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')  # Ensure the app runs on all available IP addresses
