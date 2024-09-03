from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from web3 import Web3

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app

# Connect to the local blockchain (Ganache)
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Load the smart contract
with open('path/to/compiled/PropertyContract.json') as f:
    contract_json = json.load(f)
    contract_abi = contract_json['abi']
    contract_address = contract_json['networks']['5777']['address']

property_contract = web3.eth.contract(address=contract_address, abi=contract_abi)