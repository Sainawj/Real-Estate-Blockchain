from pymongo import MongoClient

# Connect to MongoDB (update with your connection string)
client = MongoClient('mongodb://localhost:27017/')

# Database and collection names
db = client['real_estate_db']
property_collection = db['properties']

# Function to insert a document
def insert_document(document):
    result = property_collection.insert_one(document)
    return result.inserted_id

# Function to retrieve documents
def get_documents(query):
    documents = property_collection.find(query)
    return list(documents)