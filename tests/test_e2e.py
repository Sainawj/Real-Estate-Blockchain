import unittest

class TestEndToEnd(unittest.TestCase):

    def test_end_to_end(self):
        # Placeholder for end-to-end testing
        self.assertTrue(True)


def test_end_to_end(client):
           
    # Step 1: User signs up
    response = client.post('/signup', json={'username': 'test_user', 'password': 'password123'})
    assert response.status_code == 201

    # Step 2: User logs in
    response = client.post('/login', json={'username': 'test_user', 'password': 'password123'})
    assert response.status_code == 200
    auth_token = response.json['token']

    # Step 3: User uploads a property
    headers = {'Authorization': f'Bearer {auth_token}'}
    property_data = {'title': 'Test Property', 'description': 'A test property', 'price': 100000}
    response = client.post('/add_property', json=property_data, headers=headers)
    assert response.status_code == 200

    # Step 4: User retrieves the property
    response = client.get('/get_properties/test_user', headers=headers)
    assert response.status_code == 200
    properties = response.json
    assert len(properties) == 1
    assert properties[0]['title'] == 'Test Property'

