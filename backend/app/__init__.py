from flask import Flask
from flask_migrate import Migrate
from os import environ, getenv

from app.extensions import db
from app.models.user_account_model import User, Profile
from app.models.content_model import Post

from app.users.routes import user_bp
from app.content.routes import post_bp

from config import DevConfig, ProdConfig

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    env_type = getenv('ENV')
    print("ENV-->", env_type)
    
    if env_type == 'development':
        config = DevConfig
    else:
        config = ProdConfig

    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    reg_blueprints(app)

    return app

def reg_blueprints(app):
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(post_bp, url_prefix='/post')
