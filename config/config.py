from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()
uri = os.getenv("MONGODB")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# db and collection
db = client.autograder
questions_collection = db.questions
answers_collection = db.answers

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
