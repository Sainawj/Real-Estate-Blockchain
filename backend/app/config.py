import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #MONGO_URI = 'mongodb://realestate_user:your_password@localhost:27017/realestate_db'