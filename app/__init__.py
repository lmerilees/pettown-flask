import app.load_env
from flask import Flask
from flask_cors import CORS
from app.config import Config
from .db import db


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)

    db.init_app(app)

    from .api.routes import bp as api_bp

    app.register_blueprint(api_bp)

    return app
