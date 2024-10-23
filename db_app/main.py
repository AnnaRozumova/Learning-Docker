from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient
import os
import time

app = Flask(__name__)

# Get MongoDB URI from environment variable
mongo_uri = os.getenv('MONGO_URI')

while True:
    try:
        client = MongoClient(mongo_uri)
        db = client["mydatabase"]
        collection = db["mycollection"]
        print("Connected to MongoDB successfully")
        break
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        time.sleep(5)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_item():
    try:
        if request.form:
            data = {
                "name": request.form.get("name"),
                "description": request.form.get("description"),
                "example": request.form.get("example")
            }
        else:
            data = request.json

        if not data:
            return jsonify({"error": "Invalid input, no data provided"}), 400
    
        collection.insert_one(data)
        return render_template('success.html', message="Item added successfully")
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An internal error occurred"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)