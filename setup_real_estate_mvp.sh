#!/bin/bash

# Set up the necessary directories and files for the project
mkdir -p ~/real_estate_blockchain/frontend/public
mkdir -p ~/real_estate_blockchain/frontend/src/components/Auth
mkdir -p ~/real_estate_blockchain/frontend/src/components/Dashboard
mkdir -p ~/real_estate_blockchain/frontend/src/components/Property
mkdir -p ~/real_estate_blockchain/frontend/src/components/Transaction
mkdir -p ~/real_estate_blockchain/frontend/src/services
mkdir -p ~/real_estate_blockchain/blockchain/contracts
mkdir -p ~/real_estate_blockchain/blockchain/migrations
mkdir -p ~/real_estate_blockchain/backend/app/routes
mkdir -p ~/real_estate_blockchain/backend/app/services
mkdir -p ~/real_estate_blockchain/backend/app/utils
mkdir -p ~/real_estate_blockchain/backend/tests
mkdir -p ~/real_estate_blockchain/docs
mkdir -p ~/real_estate_blockchain/storage/ipfs
mkdir -p ~/real_estate_blockchain/storage/mongodb

# Install necessary dependencies for the system
sudo apt update
sudo apt install -y python3-pip python3-venv mongodb npm nodejs docker.io docker-compose

# Install Truffle globally for blockchain development
sudo npm install -g truffle

# Set up Python virtual environment
cd ~/real_estate_blockchain/backend
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install Flask Flask-PyMongo Web3

# Create requirements.txt for Flask backend
echo "Flask
Flask-PyMongo
Web3" > requirements.txt

# Initialize a new React project for the frontend
cd ~/real_estate_blockchain/frontend
npx create-react-app .

# Install additional frontend dependencies
npm install axios

# Set up Truffle for blockchain development
cd ~/real_estate_blockchain/blockchain
truffle init

# Create Dockerfiles
echo "FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [\"python3\", \"-m\", \"flask\", \"run\", \"--host=0.0.0.0\"]" > ~/real_estate_blockchain/backend/Dockerfile

echo "FROM node:14
WORKDIR /app
COPY . .
RUN npm install
CMD [\"npm\", \"start\"]" > ~/real_estate_blockchain/frontend/Dockerfile

# Write frontend files
cat <<EOT > ~/real_estate_blockchain/frontend/public/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Real Estate Blockchain MVP</title>
</head>
<body>
    <div id="root"></div>
</body>
</html>
EOT

cat <<EOT > ~/real_estate_blockchain/frontend/src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Auth from './components/Auth/Auth';
import Dashboard from './components/Dashboard/Dashboard';
import Property from './components/Property/Property';
import Transaction from './components/Transaction/Transaction';

function App() {
    return (
        <Router>
            <Switch>
                <Route path="/auth" component={Auth} />
                <Route path="/dashboard" component={Dashboard} />
                <Route path="/property" component={Property} />
                <Route path="/transaction" component={Transaction} />
            </Switch>
        </Router>
    );
}

export default App;
EOT

# Write example Auth component
cat <<EOT > ~/real_estate_blockchain/frontend/src/components/Auth/Auth.js
import React from 'react';

function Auth() {
    return (
        <div>
            <h1>Login</h1>
            <form>
                <label>Email: <input type="email" name="email" /></label>
                <label>Password: <input type="password" name="password" /></label>
                <button type="submit">Login</button>
            </form>
        </div>
    );
}

export default Auth;
EOT

# Write example Dashboard component
cat <<EOT > ~/real_estate_blockchain/frontend/src/components/Dashboard/Dashboard.js
import React from 'react';

function Dashboard() {
    return (
        <div>
            <h1>User Dashboard</h1>
            <div>
                <h2>User Information</h2>
                <p>Full Names: John Doe</p>
                <p>Location: Nairobi, Kenya</p>
                <p>Email Address: john.doe@example.com</p>
                <p>Phone: +254700123456</p>
                <p>Properties Owned: 2</p>
                <p>Properties Leased: 1</p>
            </div>
        </div>
    );
}

export default Dashboard;
EOT

# Backend Setup: Write Python/Flask files
cat <<EOT > ~/real_estate_blockchain/backend/app/__init__.py
from flask import Flask
from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    mongo.init_app(app)
    
    from .routes import auth_routes, property_routes, contract_routes
    app.register_blueprint(auth_routes.auth_bp)
    app.register_blueprint(property_routes.property_bp)
    app.register_blueprint(contract_routes.contract_bp)
    
    return app
EOT

cat <<EOT > ~/real_estate_blockchain/backend/app/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGO_URI = 'mongodb://realestate_user:your_password@localhost:27017/realestate_db'
EOT

# Write simple models, routes, and services
cat <<EOT > ~/real_estate_blockchain/backend/app/models.py
from flask_pymongo import PyMongo
from bson import ObjectId

mongo = PyMongo()

class User:
    def __init__(self, data):
        self.id = str(data.get('_id'))
        self.full_name = data.get('full_name')
        self.location = data.get('location')
        self.email = data.get('email')
        self.phone = data.get('phone')
        self.properties_owned = data.get('properties_owned', [])
        self.properties_leased = data.get('properties_leased', [])
        self.watchlist = data.get('watchlist', [])

    @staticmethod
    def get_by_id(user_id):
        data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return User(data) if data else None

    @staticmethod
    def create(user_data):
        return mongo.db.users.insert_one(user_data).inserted_id
EOT

# Write a simple Solidity contract for RealEstate
cat <<EOT > ~/real_estate_blockchain/blockchain/contracts/RealEstate.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RealEstate {
    struct Property {
        uint id;
        string name;
        address owner;
    }

    Property[] public properties;
    uint public propertyCount;

    function addProperty(string memory name) public {
        properties.push(Property(propertyCount, name, msg.sender));
        propertyCount++;
    }

    function getProperty(uint id) public view returns (Property memory) {
        require(id < propertyCount, "Property does not exist");
        return properties[id];
    }
}
EOT

cat <<EOT > ~/real_estate_blockchain/blockchain/migrations/deploy_contract.js
const RealEstate = artifacts.require("RealEstate");

module.exports = function(deployer) {
  deployer.deploy(RealEstate);
};
EOT

cat <<EOT > ~/real_estate_blockchain/blockchain/truffle-config.js
module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 8545,
      network_id: "*"
    }
  },
  compilers: {
    solc: {
      version: "0.8.0"
    }
  }
};
EOT

# Set up MongoDB User and Database
mongo <<EOF
use admin
use realestate_db
db.createUser({
  user: "realestate_user",
  pwd: "your_password",
  roles: [{ role: "readWrite", db: "realestate_db" }]
})
EOF

# Initialize and Deploy the Solidity Contract
cd ~/real_estate_blockchain/blockchain
truffle compile
truffle migrate

# Start MongoDB, Flask Backend, and React Frontend using Docker
cd ~/real_estate_blockchain
sudo docker-compose up --build -d

# Open the web browser to access the project
xdg-open "http://localhost:3000"
