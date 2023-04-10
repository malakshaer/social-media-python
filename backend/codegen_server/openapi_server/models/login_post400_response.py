# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class LoginPost400Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message=None):  # noqa: E501
        """LoginPost400Response - a model defined in OpenAPI

        :param message: The message of this LoginPost400Response.  # noqa: E501
        :type message: str
        """
        self.openapi_types = {
            'message': str
        }

        self.attribute_map = {
            'message': 'message'
        }

        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'LoginPost400Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _login_post_400_response of this LoginPost400Response.  # noqa: E501
        :rtype: LoginPost400Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self):
        """Gets the message of this LoginPost400Response.

        The error message.  # noqa: E501

        :return: The message of this LoginPost400Response.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this LoginPost400Response.

        The error message.  # noqa: E501

        :param message: The message of this LoginPost400Response.
        :type message: str
        """

        self._message = message
