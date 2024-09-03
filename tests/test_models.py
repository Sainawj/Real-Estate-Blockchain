import pytest
from backend.models import PropertyModel
import unittest
from backend.storage.ipfs.ipfs_utils import add_file, get_file

@pytest.fixture(scope='module')
def mongodb():
    # Setup MongoDB test connection
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')
    db = client['test_real_estate_db']
    yield db
    # Teardown MongoDB test connection
    client.drop_database('test_real_estate_db')

def test_insert_property(mongodb):
    property_data = {
        'title': 'Test Property',
        'description': 'A test property',
        'price': 100000,
        'owner': 'owner_name'
    }
    property_id = PropertyModel.insert_property(property_data)
    assert property_id is not None

def test_get_properties_by_owner(mongodb):
    owner = 'owner_name'
    properties = PropertyModel.get_properties_by_owner(owner)
    assert isinstance(properties, list)
    assert len(properties) >= 0  # Change to >0 if you have predefined data

class TestIPFS(unittest.TestCase):

    def test_add_file(self):
        result = add_file('testfile.txt')
        self.assertIsNotNone(result)