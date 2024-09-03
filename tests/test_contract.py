import unittest
from backend.blockchain.contract import deploy_contract, create_property, get_property
from backend.blockchain.contract import create_property, get_property

def test_deploy_contract():
    contract_address = deploy_contract()
    assert contract_address is not None

def test_create_property():
    contract_address = deploy_contract()
    property_id = create_property(contract_address, "Test Property", 100000)
    assert property_id is not None

def test_get_property():
    contract_address = deploy_contract()
    property_id = create_property(contract_address, "Test Property", 100000)
    property_details = get_property(contract_address, property_id)
    assert property_details['title'] == "Test Property"

class TestContract(unittest.TestCase):

    def test_create_property(self):
        tx_receipt = create_property("Test Property", 100)
        self.assertIsNotNone(tx_receipt)

    def test_get_property(self):
        property_data = get_property(1)
        self.assertIsNotNone(property_data)