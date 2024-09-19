from flask import Flask, request, jsonify
import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

BASEDIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, 'dev_socialmedia.db')
db = SQLAlchemy()
Migrate(app, db)

@app.route('/', methods=['GET'])
def hello():
    message = {
        'text': 'Hello, World!'
    }
    return jsonify(message), 200

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

@app.route('/users', methods=['GET'])
def get_all_accounts():
    return jsonify(demo_users), 200
    
@app.route('/newuser', methods=['POST'])
def add_new_user():
    if request.is_json:
        data = request.get_json()
        fname = data.get('fname')
        lname = data.get('lname')
        return jsonify({"message": "User data received", "fname": fname, "lname": lname}), 200
    else:
        return jsonify({'error': 'Request must be JSON'}), 400

if __name__ == '__main__':
    app.run(debug=True)
