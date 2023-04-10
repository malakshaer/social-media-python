# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.private_put200_response import PrivatePut200Response  # noqa: E501
from openapi_server.models.update_profile_put200_response import UpdateProfilePut200Response  # noqa: E501
from openapi_server.models.update_profile_put401_response import UpdateProfilePut401Response  # noqa: E501
from openapi_server.models.update_profile_put404_response import UpdateProfilePut404Response  # noqa: E501
from openapi_server.models.update_profile_put_request import UpdateProfilePutRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_accept_user_id_post(self):
        """Test case for accept_user_id_post

        Accept a follow request
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/accept/{user_id}'.format(user_id='user_id_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_request_user_id_delete(self):
        """Test case for delete_request_user_id_delete

        Delete a follow request
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/delete-request/{user_id}'.format(user_id='user_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_follow_user_id_post(self):
        """Test case for follow_user_id_post

        Follow a user
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/follow/{user_id}'.format(user_id='user_id_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_users_get(self):
        """Test case for get_all_users_get

        Get a list of all users
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/get-all-users',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_followers_get(self):
        """Test case for get_followers_get

        Get a list of followers
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/get-followers',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_following_get(self):
        """Test case for get_following_get

        Get a list of users being followed
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/get-following',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_request_list_get(self):
        """Test case for get_request_list_get

        Get a list of follow requests
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/get-request-list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_sent_requests_get(self):
        """Test case for get_sent_requests_get

        Get a list of sent follow requests
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/get-sent-requests',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_user_info_user_id_get(self):
        """Test case for get_user_info_user_id_get

        Get user info
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/get-user-info/{user_id}'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_private_put(self):
        """Test case for private_put

        Toggle the privacy setting of the current user's account.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/private',
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_follower_user_id_post(self):
        """Test case for remove_follower_user_id_post

        Remove a follower
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/remove-follower/{user_id}'.format(user_id='user_id_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_unfollow_user_id_put(self):
        """Test case for unfollow_user_id_put

        Unfollow a user
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/unfollow/{user_id}'.format(user_id='user_id_example'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_profile_put(self):
        """Test case for update_profile_put

        Update user profile
        """
        update_profile_put_request = openapi_server.UpdateProfilePutRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/update-profile',
            method='PUT',
            headers=headers,
            data=json.dumps(update_profile_put_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
