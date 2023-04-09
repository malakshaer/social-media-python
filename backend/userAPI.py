from bson import ObjectId
from flask import jsonify, request
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from pymongo import ReturnDocument
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
import datetime
import base64

user = Blueprint('userAPI', __name__)

mongo = PyMongo()


@user.record
def record(state):
    global mongo
    mongo.init_app(state.app)


@user.route('/update-profile', methods=['PUT'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    if not user:
        return jsonify({'message': 'User not found'}), 404

    data = request.json
    first_name = data.get('firstName', user['firstName'])
    last_name = data.get('lastName', user['lastName'])
    bio = data.get('bio', user['bio'])
    image = data.get('image', user.get('image'))

    if image:
        # if an image was uploaded, save it to the user's profile
        image_data = base64.b64decode(image.split(',')[1])
        mongo.db.users.update_one({'_id': ObjectId(user_id)}, {
            '$set': {
                'image': image_data
            }
        })

    # update the user profile
    mongo.db.users.update_one({'_id': ObjectId(user_id)}, {
        '$set': {
            'firstName': first_name,
            'lastName': last_name,
            'bio': bio
        }
    })

    return jsonify({'message': 'Profile updated successfully'}), 200


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

    if not is_private:
        return jsonify({'message': 'Account is now private.', 'isPrivate': True}), 200
    else:
        return jsonify({'message': 'Account is now public.', 'isPrivate': False}), 200


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


@user.route('/remove-follower/<user_id>', methods=['POST'])
@jwt_required()
def remove_follower(user_id):
    # Get the current user's ID and information
    current_user_id = get_jwt_identity()
    current_user = mongo.db.users.find_one({'_id': ObjectId(current_user_id)})
    current_user_name = current_user['firstName'] + \
        ' ' + current_user['lastName']

    # Get the user to be removed's information
    user_to_remove = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    user_to_remove_name = user_to_remove['firstName'] + \
        ' ' + user_to_remove['lastName']

    # Check if the current user is following the user to be removed
    request = None
    for req in current_user['followers']:
        if req['id'] == user_id:
            request = req
            break
    if not request:
        return jsonify({'message': 'This user is not following you.'}), 400

    # Remove the user to be removed from the current user's follower's list
    mongo.db.users.update_one(
        {'_id': ObjectId(current_user_id)},
        {'$pull': {'followers': {'id': user_id, 'name': user_to_remove_name}}}
    )

    # Remove the current user from the user to be removed's following list
    mongo.db.users.update_one(
        {'_id': ObjectId(user_id)},
        {'$pull': {'following': {'id': current_user_id, 'name': current_user_name}}}
    )

    return jsonify({'message': f'You have removed {user_to_remove_name}.'})


@user.route('/get-followers', methods=['GET'])
@jwt_required()
def get_followers():
    # Get the current user's ID and information
    current_user_id = get_jwt_identity()
    current_user = mongo.db.users.find_one({'_id': ObjectId(current_user_id)})

    # Get the list of users following the current user
    followers = []
    for follower in current_user['followers']:
        follower_id = ObjectId(follower['id'])
        follower_info = mongo.db.users.find_one({'_id': follower_id})
        follower_name = follower_info['firstName'] + \
            ' ' + follower_info['lastName']
        follower_image = follower_info.get('image', None)
        if follower_image:
            follower_image = base64.b64encode(follower_image).decode('utf-8')
        followers.append(
            {'id': str(follower_id), 'name': follower_name, 'image': follower_image})

    return jsonify({'followers': followers})


@user.route('/get-following', methods=['GET'])
@jwt_required()
def get_following():
    # Get the current user's ID and information
    current_user_id = get_jwt_identity()
    current_user = mongo.db.users.find_one({'_id': ObjectId(current_user_id)})

    # Get the list of users following the current user
    following = []
    for follower in current_user['following']:
        follower_id = ObjectId(follower['id'])
        follower_info = mongo.db.users.find_one({'_id': follower_id})
        follower_name = follower_info['firstName'] + \
            ' ' + follower_info['lastName']
        follower_image = follower_info.get('image', None)
        if follower_image:
            follower_image = base64.b64encode(follower_image).decode('utf-8')
        following.append(
            {'id': str(follower_id), 'name': follower_name, 'image': follower_image})

    return jsonify({'following': following})


@user.route('/get-request-list', methods=['GET'])
@jwt_required()
def get_request_list():
    # Get the current user's ID and information
    current_user_id = get_jwt_identity()
    current_user = mongo.db.users.find_one({'_id': ObjectId(current_user_id)})

    # Get the list of users following the current user
    request_list = []
    for follower in current_user['request_list']:
        follower_id = ObjectId(follower['id'])
        follower_info = mongo.db.users.find_one({'_id': follower_id})
        follower_name = follower_info['firstName'] + \
            ' ' + follower_info['lastName']
        follower_image = follower_info.get('image', None)
        if follower_image:
            follower_image = base64.b64encode(follower_image).decode('utf-8')
        request_list.append(
            {'id': str(follower_id), 'name': follower_name, 'image': follower_image})

    return jsonify({'requestList': request_list})


@user.route('/get-sent-requests', methods=['GET'])
@jwt_required()
def get_sent_requests():
    # Get the current user's ID and information
    current_user_id = get_jwt_identity()
    current_user = mongo.db.users.find_one({'_id': ObjectId(current_user_id)})

    # Get the list of users following the current user
    sent_requests = []
    for follower in current_user['requested']:
        follower_id = ObjectId(follower['id'])
        follower_info = mongo.db.users.find_one({'_id': follower_id})
        follower_name = follower_info['firstName'] + \
            ' ' + follower_info['lastName']
        follower_image = follower_info.get('image', None)
        if follower_image:
            follower_image = base64.b64encode(follower_image).decode('utf-8')
        sent_requests.append(
            {'id': str(follower_id), 'name': follower_name, 'image': follower_image})

    return jsonify({'requestList': sent_requests})


@user.route('/upload', methods=['POST'])
@jwt_required()
def upload_image():
    # Get the base64-encoded image data from the request
    image_data = request.json['image_data']

    # Convert the base64-encoded image data to bytes
    image_bytes = base64.b64decode(image_data)

    # Upload the image to the database
    mongo.db.users.insert_one({'name': 'profileImage', 'data': image_bytes})

    return jsonify({'success': True})


@user.route('/get-user-info', methods=['GET'])
@jwt_required()
def get_user_info():
    # Get current user from token
    token = request.headers.get('Authorization').split()[1]
    current_user = mongo.db.users.find_one({'tokens.token': token})

    if current_user:
        # Retrieve number of followers and following
        num_followers = len(current_user.get('followers', []))
        num_following = len(current_user.get('following', []))

        # Retrieve profile image as base64 string
        image = ''
        if current_user.get('image'):
            image = base64.b64encode(current_user['image']).decode('utf-8')

        # Retrieve following and requested lists
        following_list = current_user.get('following', [])
        requested_list = current_user.get('requested', [])

        # Return user info
        return jsonify({
            'id': str(current_user['_id']),
            'firstName': current_user.get('firstName', ''),
            'lastName': current_user.get('lastName', ''),
            'numberFollowers': num_followers,
            'numberFollowing': num_following,
            'bio': current_user.get('bio', ''),
            'is_private': current_user.get('is_private', ''),
            'image': image,
            'following_list': following_list,
            'requested_list': requested_list
        })
    else:
        return jsonify({'message': 'User not found.'}), 404


@user.route('/get-all-users', methods=['GET'])
def get_all_users():
    users = mongo.db.users.find(
        {}, {'firstName': 1, 'lastName': 1, 'followers': 1, 'following': 1, 'bio': 1, 'image': 1})

    result = []
    for user in users:
        user['_id'] = str(user['_id'])
        user['num_followers'] = len(user['followers'])
        user['num_following'] = len(user['following'])
        if user.get('image'):
            encoded_image = base64.b64encode(user['image']).decode('utf-8')
            user['image'] = f"data:image/jpeg;base64,{encoded_image}"
        result.append(user)

    return jsonify(result)
