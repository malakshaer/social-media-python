from flask import Blueprint, request, jsonify, session
import bcrypt
import jwt
from flask_pymongo import PyMongo
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required

auth = Blueprint('authAPI', __name__)

mongo = PyMongo()


@auth.record
def record(state):
    global mongo
    mongo.init_app(state.app)


@auth.route('/register', methods=['POST'])
def register():
    # Get user input
    firstName = request.json['firstName']
    lastName = request.json['lastName']
    email = request.json['email']
    password = request.json['password']
    confirmPassword = request.json['confirmPassword']

    # Check if email already exists
    if mongo.db.users.find_one({'email': email}):
        return jsonify({'message': 'Email already exists'})

    # Check if passwords match
    if password != confirmPassword:
        return jsonify({'message': 'Passwords do not match'})

    # Hash the password
    hashed_password1 = bcrypt.hashpw(
        password.encode('utf-8'), bcrypt.gensalt())

    hashed_password2 = bcrypt.hashpw(
        confirmPassword.encode('utf-8'), bcrypt.gensalt())

    # Create token
    access_token = create_access_token(identity=email)

    # Insert the new user into the database
    mongo.db.users.insert_one({
        'firstName': firstName,
        'lastName': lastName,
        'email': email,
        'password': hashed_password1,
        'confirmPassword': hashed_password2,
        'tokens': [
            {
                'token': str(access_token)
            }
        ]
    }).inserted_id

    # Return success message with token
    return jsonify({
        'message': 'User created successfully',
        'token': str(access_token)
    }), 200


@auth.route('/login', methods=['POST'])
def login():

    # Check if user is already logged in
    if 'user_id' in session:
        return jsonify({'message': 'User already logged in.'}), 400

    # Get the user input
    email = request.json['email']
    password = request.json['password']

    # Check if email exists
    user = mongo.db.users.find_one({'email': email})
    if not user:
        return jsonify({'message': 'Invalid email or password.'}), 401

    # Check if password is correct
    if bcrypt.checkpw(password.encode('utf-8'), user['password']):
        # Store user id in session
        session['user_id'] = str(user['_id'])

        # Generate a JWT token
        access_token = create_access_token(identity=email)

        # Return success message with token
        return jsonify({
            'message': 'You are logged in.',
            'token': str(access_token)
        }), 201

    return jsonify({'message': 'Invalid email or password.'}), 401


@auth.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully.'}), 200
