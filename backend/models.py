from flask_mongoengine import MongoEngine

db = MongoEngine()

class Property(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    price = db.FloatField(required=True)