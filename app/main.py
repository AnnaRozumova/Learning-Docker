from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Get MongoDB URI from environment variable
mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client["mydatabase"]
collection = db["mycollection"]

@app.route('/search', methods=['GET'])
def search_items():
    try:
        query = request.args.get('query')
        if not query:
            return jsonify({"error": "No search query provided"}), 400

        # Perform search in MongoDB using regex
        result = collection.find({"item_name": {"$regex": query, "$options": "i"}})
        items = list(result)

        # Convert ObjectId to string for JSON response
        for item in items:
            item["_id"] = str(item["_id"])

        return jsonify(items), 200

    except Exception as e:
        print(f"Error during search: {e}")  # Log the error to the console (check docker logs)
        return jsonify({"error": "An internal error occurred"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
