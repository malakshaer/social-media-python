# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class PrivatePut200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message=None, is_private=None):  # noqa: E501
        """PrivatePut200Response - a model defined in OpenAPI

        :param message: The message of this PrivatePut200Response.  # noqa: E501
        :type message: str
        :param is_private: The is_private of this PrivatePut200Response.  # noqa: E501
        :type is_private: bool
        """
        self.openapi_types = {
            'message': str,
            'is_private': bool
        }

        self.attribute_map = {
            'message': 'message',
            'is_private': 'isPrivate'
        }

        self._message = message
        self._is_private = is_private

    @classmethod
    def from_dict(cls, dikt) -> 'PrivatePut200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _private_put_200_response of this PrivatePut200Response.  # noqa: E501
        :rtype: PrivatePut200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self):
        """Gets the message of this PrivatePut200Response.

        A message indicating the success or failure of the operation.  # noqa: E501

        :return: The message of this PrivatePut200Response.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PrivatePut200Response.

        A message indicating the success or failure of the operation.  # noqa: E501

        :param message: The message of this PrivatePut200Response.
        :type message: str
        """

        self._message = message

    @property
    def is_private(self):
        """Gets the is_private of this PrivatePut200Response.

        The new privacy status of the account.  # noqa: E501

        :return: The is_private of this PrivatePut200Response.
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """Sets the is_private of this PrivatePut200Response.

        The new privacy status of the account.  # noqa: E501

        :param is_private: The is_private of this PrivatePut200Response.
        :type is_private: bool
        """

        self._is_private = is_private
