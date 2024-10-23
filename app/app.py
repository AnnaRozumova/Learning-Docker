from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

# Get MongoDB URI from environment variable
mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client["mydatabase"]
collection = db["mycollection"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_items():
    try:
        query = request.args.get('query')
        if not query:
            return render_template('message.html', message="No search query provided")

        # Perform search in MongoDB using regex
        result = collection.find({"name": {"$regex": query, "$options": "i"}})
        items = list(result)

        # Convert ObjectId to string for JSON response
        for item in items:
            item["_id"] = str(item["_id"])

        return jsonify(items), 200

    except Exception as e:
        print(f"Error during search: {e}")
        return render_template('message.html', message="An internal error occurred"), 500

@app.route('/update/<id>', methods=['GET', 'POST'])
def update_item(id):
    if request.method == 'GET':
        # Retrieve the item by id and display it in a form
        item = collection.find_one({"_id": ObjectId(id)})
        if item:
            return render_template('update.html', item=item)
        else:
            return render_template('message.html', message="Item not found")

    elif request.method == 'POST':
        # Update the item in the database
        name = request.form.get('name')
        description = request.form.get('description')
        example = request.form.get('example')

        collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "name": name,
                "description": description,
                "example": example
            }}
        )
        return render_template('message.html', message="Item updated successfully!")

@app.route('/delete/<id>', methods=['POST'])
def delete_item(id):
    try:
        # Delete the item by id
        result = collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 1:
            return render_template('message.html', message="Item deleted successfully!")
        else:
            return render_template('message.html', message="Item not found")
    except Exception as e:
        print(f"Error during deletion: {e}")
        return render_template('message.html', message="An internal error occurred"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

