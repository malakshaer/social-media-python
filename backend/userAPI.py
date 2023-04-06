from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from pymongo import ReturnDocument
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import datetime

user = Blueprint('userAPI', __name__)

mongo = PyMongo()


@user.record
def record(state):
    global mongo
    mongo.init_app(state.app)


@user.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    # Get the user ID from the JWT token
    current_user_id = get_jwt_identity()

    # Query the user document from the database
    user = mongo.db.users.find_one({'_id': ObjectId(current_user_id)})

    # Check if user exists
    if not user:
        return jsonify({'message': 'User not found.'}), 404

    # Serialize user document to JSON and return it
    user_data = {
        'firstName': user['firstName'],
        'lastName': user['lastName'],
        'email': user['email'],
        'followers': user['followers'],
        'following': user['following'],
        'is_private': user['is_private']
    }

    return jsonify(user_data), 200
