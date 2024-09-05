from app.utils.blockchain import Blockchain

def deploy_contract():
    blockchain = Blockchain()
    return blockchain.deploy_contract()

def interact_contract(data):
    blockchain = Blockchain()
    return blockchain.interact_with_contract(data['method'], data['params'])