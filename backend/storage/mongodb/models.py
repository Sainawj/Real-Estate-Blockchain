from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['real_estate_db']
property_collection = db['properties']

class PropertyModel:
    @staticmethod
    def insert_property(property_data):
        result = property_collection.insert_one(property_data)
        return result.inserted_id

    @staticmethod
    def get_properties_by_owner(owner):
        return list(property_collection.find({'owner': owner}))

    @staticmethod
    def get_property_by_id(property_id):
        return property_collection.find_one({'_id': property_id})

property_schema = {
    'title': 'string',
    'description': 'string',
    'price': 'float',
    'owner': 'string',
    'ipfs_hash': 'string'  # Reference to the IPFS stored file
}