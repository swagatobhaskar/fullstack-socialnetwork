from flask import Flask
from flask_migrate import Migrate

from app.extensions import db
from app.models.user_account_model import User

from app.users.routes import user_bp

from config import DevConfig

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # config condition
    app.config.from_object(DevConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    reg_blueprints(app)

    return app

def reg_blueprints(app):
    app.register_blueprint(user_bp, url_prefix='/user')
    