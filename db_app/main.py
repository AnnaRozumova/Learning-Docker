from pymongo import MongoClient
from faker import Faker
import random
import os
import time

# Get MongoDB URI from environment variable
mongo_uri = os.getenv('MONGO_URI')

# Retry connecting to MongoDB
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

# Only initialize data if the collection is empty
if collection.count_documents({}) == 0:
    fake = Faker()
    sample_data = []

    for i in range(1000):
        item = {
            "name": fake.word().capitalize(),
            "description": fake.sentence(),
            "example": fake.paragraph(),
        }
        sample_data.append(item)

    collection.insert_many(sample_data)
    print("New sample data initialized in MongoDB.")
else:
    print("Collection already contains data. Skipping initialization.")
