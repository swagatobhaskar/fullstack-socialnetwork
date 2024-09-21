from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
import enum

from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    profile = db.relationship('Profile', uselist=False, back_populates='user')

    def __repr__(self):
        return f"{self.id} | {self.email}"
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class SexEnum(enum.Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=True)
    username = db.Column(db.String(30), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    sex = db.Column(db.Enum(SexEnum), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    region = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    area = db.Column(db.String(100), nullable=True)
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='profile')

    def __repr__(self):
        return f'{self.id} | {self.fname} {self.lname} | {self.user.email} | {self.sex.value}'
