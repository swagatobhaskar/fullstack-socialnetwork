from flask_sqlalchemy import SQLAlchemy
from sqlalchemy .sql import func
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    def __repr__(self):
        return f"{self.id} | {self.email}"
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
