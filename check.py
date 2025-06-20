from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(os.getenv("MONGO_DB_URL"))
db = client["PRATYAKSH"]
collection = db["NetworkData"]
print(collection.count_documents({}))
