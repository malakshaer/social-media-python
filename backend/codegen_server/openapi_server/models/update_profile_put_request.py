# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class UpdateProfilePutRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, first_name=None, last_name=None, bio=None, image=None):  # noqa: E501
        """UpdateProfilePutRequest - a model defined in OpenAPI

        :param first_name: The first_name of this UpdateProfilePutRequest.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this UpdateProfilePutRequest.  # noqa: E501
        :type last_name: str
        :param bio: The bio of this UpdateProfilePutRequest.  # noqa: E501
        :type bio: str
        :param image: The image of this UpdateProfilePutRequest.  # noqa: E501
        :type image: str
        """
        self.openapi_types = {
            'first_name': str,
            'last_name': str,
            'bio': str,
            'image': str
        }

        self.attribute_map = {
            'first_name': 'firstName',
            'last_name': 'lastName',
            'bio': 'bio',
            'image': 'image'
        }

        self._first_name = first_name
        self._last_name = last_name
        self._bio = bio
        self._image = image

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateProfilePutRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _update_profile_put_request of this UpdateProfilePutRequest.  # noqa: E501
        :rtype: UpdateProfilePutRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def first_name(self):
        """Gets the first_name of this UpdateProfilePutRequest.

        The user's new first name.  # noqa: E501

        :return: The first_name of this UpdateProfilePutRequest.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UpdateProfilePutRequest.

        The user's new first name.  # noqa: E501

        :param first_name: The first_name of this UpdateProfilePutRequest.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UpdateProfilePutRequest.

        The user's new last name.  # noqa: E501

        :return: The last_name of this UpdateProfilePutRequest.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UpdateProfilePutRequest.

        The user's new last name.  # noqa: E501

        :param last_name: The last_name of this UpdateProfilePutRequest.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def bio(self):
        """Gets the bio of this UpdateProfilePutRequest.

        The user's new bio.  # noqa: E501

        :return: The bio of this UpdateProfilePutRequest.
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio):
        """Sets the bio of this UpdateProfilePutRequest.

        The user's new bio.  # noqa: E501

        :param bio: The bio of this UpdateProfilePutRequest.
        :type bio: str
        """

        self._bio = bio

    @property
    def image(self):
        """Gets the image of this UpdateProfilePutRequest.

        The user's new profile image as a base64-encoded string.  # noqa: E501

        :return: The image of this UpdateProfilePutRequest.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this UpdateProfilePutRequest.

        The user's new profile image as a base64-encoded string.  # noqa: E501

        :param image: The image of this UpdateProfilePutRequest.
        :type image: str
        """

        self._image = image