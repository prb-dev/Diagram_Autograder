from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://prabashwarakulathunga:JwF4QtpLSHh6919S@autograder.uum3b.mongodb.net/?retryWrites=true&w=majority&appName=autograder"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# db and collection
db = client.autograder
questions_collection = db.questions

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)