from app.models import db, Property, Transaction
from datetime import datetime

def list_property(data):
    property = Property(name=data['name'], location=data['location'], owner_id=data['owner_id'], price=data['price'])
    db.session.add(property)
    db.session.commit()
    return property

def get_properties():
    return Property.query.all()

def purchase_property(property_id, data):
    property = Property.query.get(property_id)
    if property and property.is_available:
        property.is_available = False
        transaction = Transaction(property_id=property.id, buyer_id=data['buyer_id'], price=property.price, timestamp=datetime.utcnow())
        db.session.add(transaction)
        db.session.commit()
        return transaction
    return None