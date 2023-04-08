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
    first_name = request.json['firstName']
    last_name = request.json['lastName']
    email = request.json['email']
    password = request.json['password']
    confirm_password = request.json['confirmPassword']

    # Check if user already exists
    user = mongo.db.users.find_one({'email': email})
    if user:
        return jsonify({'message': 'User already exists.'}), 409

    # Check if passwords match
    if password != confirm_password:
        return jsonify({'message': 'Passwords do not match.'}), 400

    # Hash password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert new user into database
    result = mongo.db.users.insert_one({
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'password': hashed_password,
        'followers': [],
        'following': [],
        'bio': "",
        'is_private': False,
    })

    # Generate access token with user ID as identity
    access_token = create_access_token(identity=str(result.inserted_id))

    # Add token to user's tokens list
    mongo.db.users.update_one(
        {'_id': result.inserted_id},
        {'$push': {'tokens': {'token': access_token}}}
    )

    # Return success message with token
    return jsonify({
        'message': 'User created.',
        'token': access_token
    }), 201


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
        # Generate a new JWT token
        access_token = create_access_token(identity=str(user['_id']))

        # Remove the last token from the user's tokens list
        mongo.db.users.update_one(
            {'_id': user['_id']},
            {'$pop': {'tokens': -1}}
        )

        # Add the new token to the user's tokens list
        mongo.db.users.update_one(
            {'_id': user['_id']},
            {'$push': {'tokens': {'token': access_token}}}
        )

        # Store user id in session
        session['user_id'] = str(user['_id'])

        # Return success message with the new token and name
        return jsonify({
            'message': 'You are logged in.',
            'token': str(access_token),
            'name': f"{user.get('firstName', '')} {user.get('lastName', '')}"
        }), 201

    return jsonify({'message': 'Invalid email or password.'}), 401


@auth.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    session.clear()
    return jsonify({'message': 'Logged out successfully.'}), 200
