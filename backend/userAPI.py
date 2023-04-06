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


@user.route('/private', methods=['PUT'])
@jwt_required()
def make_account_private():
    current_user_id = get_jwt_identity()

    # Get the user's current privacy setting
    user = mongo.db.users.find_one({'_id': ObjectId(current_user_id)})
    is_private = user.get('is_private', False)

    # Toggle the user's privacy setting
    mongo.db.users.update_one(
        {'_id': ObjectId(current_user_id)},
        {'$set': {'is_private': not is_private}}
    )

    if is_private:
        return jsonify({'message': 'Account is now public.'}), 200
    else:
        return jsonify({'message': 'Account is now private.'}), 200


@user.route('/follow/<user_id>', methods=['POST'])
@jwt_required()
def follow_user(user_id):
    # Get the current user's ID and information
    current_user_id = get_jwt_identity()
    current_user = mongo.db.users.find_one({'_id': ObjectId(current_user_id)})
    current_user_name = current_user['firstName'] + \
        ' ' + current_user['lastName']

    # Get the user being followed's information
    user_to_follow = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    user_to_follow_name = user_to_follow['firstName'] + \
        ' ' + user_to_follow['lastName']
    is_private = user_to_follow.get('is_private', False)

    # Check if the current user is already following the other user
    if user_id in current_user['following']:
        return jsonify({'message': 'You are already following this user.'}), 400

    # Check if the current user has already sent a follow request to the other user
    if any(request['id'] == user_id for request in current_user.get('requested', [])):
        return jsonify({'message': 'Follow request already sent.'}), 400

    # If the user being followed is private, send a follow request
    if is_private:
        notification = {
            'message': f'{current_user_name} wants to follow you.',
            'sender': current_user_id,
            'receiver': user_id,
            'type': 'follow_request'
        }
        mongo.db.notifications.insert_one(notification)

        # Create a requested list in the current user document and add the user ID and name of the user they requested to follow
        mongo.db.users.update_one(
            {'_id': ObjectId(current_user_id)},
            {'$push': {'requested': {'id': user_id, 'name': user_to_follow_name}}}
        )

        # Create a request list in the other user document and add the user ID and name of the user who requested to follow
        mongo.db.users.update_one(
            {'_id': ObjectId(user_id)},
            {'$push': {'request_list': {'id': current_user_id, 'name': current_user_name}}}
        )

        return jsonify({'message': 'Follow request sent.'}), 200

    # Add the current user to the other user's followers list
    mongo.db.users.update_one(
        {'_id': ObjectId(user_id)},
        {'$push': {'followers': {'id': current_user_id, 'name': current_user_name}}}
    )

    # Add the other user to the current user's following list
    mongo.db.users.update_one(
        {'_id': ObjectId(current_user_id)},
        {'$push': {'following': {'id': user_id, 'name': user_to_follow_name}}}
    )

    return jsonify({'message': 'User followed successfully.'}), 200


@user.route('/unfollow/<user_id>', methods=['PUT'])
@jwt_required()
def unfollow_user(user_id):
    current_user_id = get_jwt_identity()

    # Check if user2 exists and is followed by user1
    user2 = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    if not user2:
        return jsonify({'message': 'User not found.'}), 404
    if {'id': str(user2['_id']), 'name': user2['firstName'] + ' ' + user2['lastName']} not in mongo.db.users.find_one({'_id': ObjectId(current_user_id)})['following']:
        return jsonify({'message': 'User is not followed.'}), 400

    # Remove user2 from current user's following list
    mongo.db.users.update_one(
        {'_id': ObjectId(current_user_id)},
        {'$pull': {'following': {'id': str(
            user2['_id']), 'name': user2['firstName'] + ' ' + user2['lastName']}}}
    )

    # Remove current user from user2's followers list
    mongo.db.users.update_one(
        {'_id': ObjectId(user_id)},
        {'$pull': {'followers': {'id': str(current_user_id), 'name': mongo.db.users.find_one({'_id': ObjectId(current_user_id)})[
            'firstName'] + ' ' + mongo.db.users.find_one({'_id': ObjectId(current_user_id)})['lastName']}}}
    )

    return jsonify({'message': 'User unfollowed successfully.'}), 200


@user.route('/delete-request/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_follow_request(user_id):
    # Get the current user's ID and information
    current_user_id = get_jwt_identity()
    current_user = mongo.db.users.find_one({'_id': ObjectId(current_user_id)})
    current_user_name = current_user['firstName'] + \
        ' ' + current_user['lastName']

    # Get the user being followed's information
    user_to_follow = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    user_to_follow_name = user_to_follow['firstName'] + \
        ' ' + user_to_follow['lastName']

    # Check if the current user has sent a follow request to the other user
    if {'id': user_id, 'name': user_to_follow_name} not in current_user['requested']:
        return jsonify({'message': 'You have not sent a follow request to this user.'}), 400

    # Remove the other user from the current user's requested list
    mongo.db.users.update_one(
        {'_id': ObjectId(current_user_id)},
        {'$pull': {'requested': {'id': user_id, 'name': user_to_follow_name}}}
    )

    # Remove the current user from the other user's request list
    mongo.db.users.update_one(
        {'_id': ObjectId(user_id)},
        {'$pull': {'request_list': {'id': current_user_id, 'name': current_user_name}}}
    )

    return jsonify({'message': 'Follow request deleted successfully.'}), 200


@user.route('/accept/<user_id>', methods=['POST'])
@jwt_required()
def accept_request(user_id):
    current_user_id = get_jwt_identity()
    current_user = mongo.db.users.find_one({'_id': ObjectId(current_user_id)})

    # Check if the current user has a request from the user to accept
    request = None
    for req in current_user['request_list']:
        if req['id'] == user_id:
            request = req
            break
    if not request:
        return jsonify({'message': 'No follow request from user.'}), 400

    # Move the user from the request_list to followers
    mongo.db.users.update_one({'_id': ObjectId(current_user_id)}, {
                              '$pull': {'request_list': request}})
    mongo.db.users.update_one({'_id': ObjectId(current_user_id)}, {
                              '$push': {'followers': request}})

    # Move the current user from requested to following
    user_to_follow = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    current_user_name = current_user['firstName'] + \
        ' ' + current_user['lastName']
    user_to_follow_name = user_to_follow['firstName'] + \
        ' ' + user_to_follow['lastName']

    mongo.db.users.update_one({'_id': ObjectId(user_id)}, {
                              '$pull': {'requested': {'id': current_user_id, 'name': current_user_name}}})
    mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$push': {'following': {
                              'id': current_user_id, 'name': current_user_name}}})

    return jsonify({'message': f'{user_to_follow_name} is following you now.'}), 200
