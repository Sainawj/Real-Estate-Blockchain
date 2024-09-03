import pytest
from backend.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_property(client):
    # Mock property data
    property_data = {
        'title': 'Test Property',
        'description': 'A test property',
        'price': 100000,
        'file_content': 'Sample file content',
        'filename': 'sample.txt'
    }
    
    # Send POST request
    response = client.post('/add_property', json=property_data)
    assert response.status_code == 200
    assert 'property_id' in response.get_json()

def test_get_properties(client):
    owner = 'owner_name'  # Replace with actual test data
    response = client.get(f'/get_properties/{owner}')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)