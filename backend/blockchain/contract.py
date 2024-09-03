from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

with open('contract_abi.json', 'r') as abi_file:
    abi = json.load(abi_file)

contract_address = "0xYourContractAddressHere"
contract = w3.eth.contract(address=contract_address, abi=abi)

def create_property(title, price):
    tx_hash = contract.functions.createProperty(title, price).transact()
    return w3.eth.wait_for_transaction_receipt(tx_hash)

def get_property(property_id):
    return contract.functions.getProperty(property_id).call()