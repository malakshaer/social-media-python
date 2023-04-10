# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.login_post201_response import LoginPost201Response  # noqa: E501
from openapi_server.models.login_post400_response import LoginPost400Response  # noqa: E501
from openapi_server.models.login_post_request import LoginPostRequest  # noqa: E501
from openapi_server.models.logout_get200_response import LogoutGet200Response  # noqa: E501
from openapi_server.models.logout_get401_response import LogoutGet401Response  # noqa: E501
from openapi_server.models.register_post201_response import RegisterPost201Response  # noqa: E501
from openapi_server.models.register_post400_response import RegisterPost400Response  # noqa: E501
from openapi_server.models.register_post409_response import RegisterPost409Response  # noqa: E501
from openapi_server.models.register_post_request import RegisterPostRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAuthenticationController(BaseTestCase):
    """AuthenticationController integration test stubs"""

    def test_login_post(self):
        """Test case for login_post

        Logs in a user.
        """
        login_post_request = openapi_server.LoginPostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/login',
            method='POST',
            headers=headers,
            data=json.dumps(login_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout_get(self):
        """Test case for logout_get

        Logs out a user.
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/logout',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_post(self):
        """Test case for register_post

        Register a new user.
        """
        register_post_request = openapi_server.RegisterPostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/register',
            method='POST',
            headers=headers,
            data=json.dumps(register_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
