from flask import render_template, url_for, flash, redirect, request, jsonify
from . import app, db, bcrypt
from .models import User, Property
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    properties = Property.query.all()
    return jsonify(properties=[property.to_dict() for property in properties])

@app.route('/register', methods=['GET', 'POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify(message="User registered successfully")

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify(message="Login successful")
    else:
        return jsonify(message="Login failed"), 401

@app.route('/logout')
def logout():
    logout_user()
    return jsonify(message="Logged out successfully")

@app.route('/property/new', methods=['POST'])
@login_required
def new_property():
    data = request.get_json()
    property = Property(title=data['title'], description=data['description'], price=data['price'], owner=current_user)
    db.session.add(property)
    db.session.commit()
    return jsonify(message="Property added successfully")

@app.route('/list_property', methods=['POST'])
@login_required
def list_property():
    data = request.get_json()
    title = data['title']
    description = data['description']
    price = web3.toWei(data['price'], 'ether')
    tx_hash = property_contract.functions.listProperty(
        title, description, price
    ).transact({'from': current_user.eth_address})
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    return jsonify({'transaction': receipt['transactionHash'].hex()})

@app.route('/buy_property/<int:property_id>', methods=['POST'])
@login_required
def buy_property(property_id):
    property = Property.query.get_or_404(property_id)
    price_in_wei = web3.toWei(property.price, 'ether')
    tx_hash = property_contract.functions.buyProperty(
        property_id
    ).transact({'from': current_user.eth_address, 'value': price_in_wei})
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    property.owner = current_user
    db.session.commit()
    return jsonify({'transaction': receipt['transactionHash'].hex()})