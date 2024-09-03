import unittest
from backend.storage.mongodb.db_config import db

def test_property_insertion(mongodb):
    property_data = {
        'title': 'Test Property',
        'description': 'This is a test',
        'price': 100000
    }
    result = mongodb.property_collection.insert_one(property_data)
    assert result.inserted_id is not None

def test_property_query(mongodb):
    property = mongodb.property_collection.find_one({'title': 'Test Property'})
    assert property is not None
    assert property['price'] == 100000

class TestDatabase(unittest.TestCase):

    def test_db_connection(self):
        collection = db.get_collection('test_collection')
        self.assertIsNotNone(collection)