from app.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

def register_user(data):
    hashed_password = generate_password_hash(data['password'])
    user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
    db.session.add(user)
    db.session.commit()
    return {'id': user.id, 'username': user.username, 'email': user.email}

def login_user(data):
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        # For simplicity, returning a mock token
        return {'token': 'mock-token'}
    return None