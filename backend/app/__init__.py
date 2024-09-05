from flask import Flask
from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    mongo.init_app(app)
    
    with app.app_context():
        from .routes import dashboard_routes, auth_routes, property_routes, contract_routes
        app.register_blueprint(dashboard_routes.dashboard_bp)
        app.register_blueprint(auth_routes.auth_bp)
        app.register_blueprint(property_routes.property_bp)
        app.register_blueprint(contract_routes.contract_bp)
        
    return app