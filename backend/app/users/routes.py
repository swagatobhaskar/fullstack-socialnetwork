from flask import request, Blueprint, jsonify, Request, url_for, redirect

from app.models.user_account_model import User, Profile

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
    
@user_bp.route('/signup', methods=['POST'])
def signup_new_user():

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


@user_bp.route('/profile/<int:id>', methods=['GET', 'PUT', 'POST'])
def user_profile(id=None):
    if request.method == 'POST':
        new_user_profile_data = request.get_json()
        new_profile = Profile(
            fname = new_user_profile_data['fname'],
            lname = new_user_profile_data['lname'],
            username = new_user_profile_data['username'],
            dob = new_user_profile_data['dob'],
            sex = new_user_profile_data['sex'],
            bio = new_user_profile_data['bio'],
            region = new_user_profile_data['region'],
            city = new_user_profile_data['city'],
            area = new_user_profile_data['area']
        )
        db.session.add(new_profile)
        db.session.commit()
        return jsonify({'message': 'Data saved successfully!'}), 201
    
    elif request.method == 'PUT':
        current_user = db.session.get(Profile, id)
        if not current_user:
            return jsonify({'error': f'User with id {id} not found!'}), 404
        
        modified_profile_data = request.get_json()
        if not modified_profile_data:
            return jsonify({"error": "Invalid data!"}), 400

        current_user.fname = modified_profile_data['fname']
        current_user.lname = modified_profile_data['lname']
        current_user.username = modified_profile_data['username']
        current_user.dob = modified_profile_data['dob']
        current_user.sex = modified_profile_data['sex']
        current_user.bio = modified_profile_data['bio']
        current_user.region = modified_profile_data['region']
        current_user.city = modified_profile_data['city']
        current_user.area = modified_profile_data['area']
        db.session.commit()
        return jsonify({'message', 'Data updated successfully!'}), 200
    
    elif request.method == 'GET':
        current_user = db.session.get(Profile, id)
        if not current_user:
            return jsonify({'error': f'User with id {id} not found!'}), 404
        
        current_user_profile = Profile.query.get(id=id)
        return jsonify(current_user_profile), 200
    