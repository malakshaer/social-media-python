import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.login_post201_response import LoginPost201Response  # noqa: E501
from openapi_server.models.login_post400_response import LoginPost400Response  # noqa: E501
from openapi_server.models.login_post_request import LoginPostRequest  # noqa: E501
from openapi_server.models.logout_get200_response import LogoutGet200Response  # noqa: E501
from openapi_server.models.logout_get401_response import LogoutGet401Response  # noqa: E501
from openapi_server.models.register_post201_response import RegisterPost201Response  # noqa: E501
from openapi_server.models.register_post400_response import RegisterPost400Response  # noqa: E501
from openapi_server.models.register_post409_response import RegisterPost409Response  # noqa: E501
from openapi_server.models.register_post_request import RegisterPostRequest  # noqa: E501
from openapi_server import util


def login_post(login_post_request):  # noqa: E501
    """Logs in a user.

     # noqa: E501

    :param login_post_request: The user&#39;s email address and password.
    :type login_post_request: dict | bytes

    :rtype: Union[LoginPost201Response, Tuple[LoginPost201Response, int], Tuple[LoginPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        login_post_request = LoginPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def logout_get():  # noqa: E501
    """Logs out a user.

     # noqa: E501


    :rtype: Union[LogoutGet200Response, Tuple[LogoutGet200Response, int], Tuple[LogoutGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def register_post(register_post_request):  # noqa: E501
    """Register a new user.

     # noqa: E501

    :param register_post_request: 
    :type register_post_request: dict | bytes

    :rtype: Union[RegisterPost201Response, Tuple[RegisterPost201Response, int], Tuple[RegisterPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        register_post_request = RegisterPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
