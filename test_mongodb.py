
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://pratyaksh1635:A635atlas.com@mongoyoutube.hles7r5.mongodb.net/?retryWrites=true&w=majority&appName=MongoYoutube"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)