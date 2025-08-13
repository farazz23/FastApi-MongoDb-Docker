
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://cman55245:dK15k7NECCn29iKR@cluster0.elwtguz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.todo_db
collection = db["todo_collection"]

def connect_to_mongo():
    try:
        client.admin.command('ping')
        print("✅ Connected to MongoDB!")
    except Exception as e:
        print(f"❌ MongoDB Connection Failed: {e}")

def close_connection():
    client.close()
    print("❌ MongoDB Connection Closed")