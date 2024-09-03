from flask import Flask
from backend.config import config
from backend.routes import init_routes
from backend.models import db

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)