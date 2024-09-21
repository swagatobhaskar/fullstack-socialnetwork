from flask import request, Blueprint, jsonify, Request, url_for, redirect

from app.models.user_account_model import User, Profile

from app.extensions import db

user_bp = Blueprint('user', __name__)