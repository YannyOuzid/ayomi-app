from pymongo import MongoClient
import os

mongodb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
client = MongoClient(mongodb_uri)

#Comment this line when you want to use pytest
db = client.npi

#Uncomment this line when you want to use pytest
#db = client.test 

collection = db["calculator"]