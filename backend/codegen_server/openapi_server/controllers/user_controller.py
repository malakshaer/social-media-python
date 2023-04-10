import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.private_put200_response import PrivatePut200Response  # noqa: E501
from openapi_server.models.update_profile_put200_response import UpdateProfilePut200Response  # noqa: E501
from openapi_server.models.update_profile_put401_response import UpdateProfilePut401Response  # noqa: E501
from openapi_server.models.update_profile_put404_response import UpdateProfilePut404Response  # noqa: E501
from openapi_server.models.update_profile_put_request import UpdateProfilePutRequest  # noqa: E501
from openapi_server import util


def accept_user_id_post(user_id):  # noqa: E501
    """Accept a follow request

    Accepts the follow request sent by the user with the specified ID. # noqa: E501

    :param user_id: The ID of the user who sent the follow request.
    :type user_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def delete_request_user_id_delete(user_id):  # noqa: E501
    """Delete a follow request

    Deletes the follow request sent to the user with the specified ID. # noqa: E501

    :param user_id: The ID of the user who sent the follow request.
    :type user_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def follow_user_id_post(user_id):  # noqa: E501
    """Follow a user

    Follows the user with the specified ID. # noqa: E501

    :param user_id: The ID of the user to follow.
    :type user_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_all_users_get():  # noqa: E501
    """Get a list of all users

    Returns a list of all users. # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_followers_get():  # noqa: E501
    """Get a list of followers

    Returns a list of followers of the current user. # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_following_get():  # noqa: E501
    """Get a list of users being followed

    Returns a list of users being followed by the current user. # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_request_list_get():  # noqa: E501
    """Get a list of follow requests

    Returns a list of follow requests sent to the current user. # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_sent_requests_get():  # noqa: E501
    """Get a list of sent follow requests

    Returns a list of follow requests sent by the current user. # noqa: E501


    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_user_info_user_id_get(user_id):  # noqa: E501
    """Get user info

    Returns the info of the user with the specified ID. # noqa: E501

    :param user_id: The ID of the user to get info for.
    :type user_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def private_put():  # noqa: E501
    """Toggle the privacy setting of the current user&#39;s account.

     # noqa: E501


    :rtype: Union[PrivatePut200Response, Tuple[PrivatePut200Response, int], Tuple[PrivatePut200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def remove_follower_user_id_post(user_id):  # noqa: E501
    """Remove a follower

    Removes the follower with the specified ID. # noqa: E501

    :param user_id: The ID of the user to remove as a follower.
    :type user_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def unfollow_user_id_put(user_id):  # noqa: E501
    """Unfollow a user

    Unfollows the user with the specified ID. # noqa: E501

    :param user_id: The ID of the user to unfollow.
    :type user_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_profile_put(update_profile_put_request):  # noqa: E501
    """Update user profile

    Updates the profile of the currently logged-in user. # noqa: E501

    :param update_profile_put_request: New user profile data
    :type update_profile_put_request: dict | bytes

    :rtype: Union[UpdateProfilePut200Response, Tuple[UpdateProfilePut200Response, int], Tuple[UpdateProfilePut200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        update_profile_put_request = UpdateProfilePutRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
