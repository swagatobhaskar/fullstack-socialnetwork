from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.ema, unique=True)