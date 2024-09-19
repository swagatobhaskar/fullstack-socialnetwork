from flask import request, Blueprint, jsonify, Request, url_for, redirect

from app.models.user_account_model import User

from app.extensions import db

user_bp = Blueprint('user', __name__)

demo_users = [
    {
        "id": 1,
        "fname": "John",
        "lname": "Doe",
        "dob": "1989-05-15",
        "city": "New York",
        "street": "123 Main St",
        "sex": "Male"
    },
    {
        "id": 2,
        "fname": "Jane",
        "lname": "Smith",
        "dob": "1985-08-25",
        "city": "Los Angeles",
        "street": "456 Elm St",
        "sex": "Female"
    },
    {
        "id": 3,
        "fname": "Emily",
        "lname": "Johnson",
        "dob": "1992-12-30",
        "city": "Chicago",
        "street": "789 Oak St",
        "sex": "Female"
    },
    {
        "id": 4,
        "fname": "Michael",
        "lname": "Brown",
        "dob": "1988-03-20",
        "city": "Houston",
        "street": "101 Pine St",
        "sex": "Male"
    },
    {
        "id": 5,
        "fname": "Sarah",
        "lname": "Davis",
        "dob": "1995-11-05",
        "city": "Phoenix",
        "street": "202 Maple St",
        "sex": "Female"
    },
    {
        "id": 6,
        "fname": "David",
        "lname": "Wilson",
        "dob": "1982-07-14",
        "city": "San Francisco",
        "street": "303 Cedar St",
        "sex": "Male"
    }
]

@user_bp.route('/users', methods=['GET'])
def get_all_accounts():
    return jsonify(demo_users), 200
    
@user_bp.route('/newuser', methods=['POST'])
def add_new_user():

    from werkzeug.security import generate_password_hash
    
    if request.is_json:
        data = request.get_json()
        email = data['email']
        password = data.get('password')

        if User.query.filter_by(email=email).first():
            return jsonify({"error": "User already exists"}), 409

        password_hash = generate_password_hash(password)
        new_user = User(email=email, password_hash=password_hash)
        
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully!"}), 200
    else:
        return jsonify({'error': 'Request must be JSON'}), 400


@user_bp.route('/', methods=['GET'])
def hello_user():
    
    return jsonify({
        'message': 'This is user BP root.'
    }), 200
