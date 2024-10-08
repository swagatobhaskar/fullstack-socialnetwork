from flask import request, Blueprint, jsonify, Request, url_for, redirect

from app.models.user_account_model import User, Profile

from app.extensions import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/login', methods=['POST'])
def user_login():
    if request.method == 'POST':
        login_data = request.get_json()
        if not login_data:
            return jsonify({'message': 'Invalid data'}), 400
        
        login_user = User.query.filter_by(email=login_data['email']).first()

        if login_user and login_user.check_password(login_data['password']):
             return jsonify({'message': 'Login successful!'}), 200
        else:
            return jsonify({'error': 'Invalid email or password!'}), 400


@user_bp.route('/signup', methods=['POST'])
def new_user_signup():
    if request.is_json:
        data = request.get_json()
        email = data['email']
        password = data.get('password')

        if User.query.filter_by(email=email).first():
            return jsonify({"error": "User already exists"}), 409

        new_user = User(email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully!"}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400


@user_bp.route('/profile', methods=['POST'])
def create_profile():
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
            area = new_user_profile_data['area'],
            user_id = new_user_profile_data['user_id'] #get current user id
        )
        db.session.add(new_profile)
        db.session.commit()
        return jsonify({'message': 'Data saved successfully!'}), 201

@user_bp.route('/profile/<int:id>', methods=['GET', 'PUT'])
def modify_profile(id):

    if request.method == 'GET':
        current_user_profile = db.session.get(Profile, id)
        if not current_user_profile:
            return jsonify({'error': f'User with id {id} not found!'}), 404
        else:
            return jsonify({
                "id": current_user_profile.id,
                "user_id": current_user_profile.user_id,
                "fname": current_user_profile.fname,
                "lname": current_user_profile.lname,
                "dob": current_user_profile.dob,
                "bio": current_user_profile.bio,
                "username": current_user_profile.username,
                "region": current_user_profile.region,
                "city": current_user_profile.city,
                "area": current_user_profile.area,
                "sex": current_user_profile.sex.value
                }), 200
        
    elif request.method == 'PUT':
        current_user_profile = db.session.get(Profile, id)
        if not current_user_profile:
            return jsonify({'error': f'User with id {id} not found!'}), 404
        
        modified_profile_data = request.get_json()
        if not modified_profile_data:
            return jsonify({"error": "Invalid data!"}), 400

        current_user_profile.fname = modified_profile_data['fname']
        current_user_profile.lname = modified_profile_data['lname']
        current_user_profile.username = modified_profile_data['username']
        current_user_profile.dob = modified_profile_data['dob']
        current_user_profile.sex = modified_profile_data['sex']
        current_user_profile.bio = modified_profile_data['bio']
        current_user_profile.region = modified_profile_data['region']
        current_user_profile.city = modified_profile_data['city']
        current_user_profile.area = modified_profile_data['area']
        db.session.commit()
        return jsonify({'message', 'Data updated successfully!'}), 200
        