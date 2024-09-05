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


class Property:
    def __init__(self, data):
        self.id = str(data.get('_id'))
        self.name = data.get('name')
        self.location = data.get('location')
        self.price = data.get('price')
        self.image_url = data.get('image_url')
        self.owner_id = str(data.get('owner_id'))

    @staticmethod
    def get_by_id(property_id):
        data = mongo.db.properties.find_one({"_id": ObjectId(property_id)})
        return Property(data) if data else None

    @staticmethod
    def create(property_data):
        return mongo.db.properties.insert_one(property_data).inserted_id


class Transaction:
    def __init__(self, data):
        self.id = str(data.get('_id'))
        self.user_id = str(data.get('user_id'))
        self.date = data.get('date')
        self.amount = data.get('amount')
        self.description = data.get('description')
        self.check = data.get('check')
        self.who = data.get('who')
        self.balance = data.get('balance')
        self.receipt = data.get('receipt')
        self.balance_paid = data.get('balance_paid')
        self.interest = data.get('interest')
        self.fees = data.get('fees')

    @staticmethod
    def get_by_user_id(user_id):
        data = mongo.db.transactions.find({"user_id": ObjectId(user_id)})
        return [Transaction(item) for item in data]