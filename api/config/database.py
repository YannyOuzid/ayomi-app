from pymongo import MongoClient
import os

MONGO_DETAILS = os.getenv("MONGO_URI", "mongodb://localhost:27017/npi")
client = MongoClient(MONGO_DETAILS)
db = client.get_default_database()

collection = db["calculator"]