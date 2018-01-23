# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InvitationCreate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, invitor_id: str=None, first_name: str=None, last_name: str=None, email: str=None, expires_at: datetime=None):  # noqa: E501
        """InvitationCreate - a model defined in Swagger

        :param invitor_id: The invitor_id of this InvitationCreate.  # noqa: E501
        :type invitor_id: str
        :param first_name: The first_name of this InvitationCreate.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this InvitationCreate.  # noqa: E501
        :type last_name: str
        :param email: The email of this InvitationCreate.  # noqa: E501
        :type email: str
        :param expires_at: The expires_at of this InvitationCreate.  # noqa: E501
        :type expires_at: datetime
        """
        self.swagger_types = {
            'invitor_id': str,
            'first_name': str,
            'last_name': str,
            'email': str,
            'expires_at': datetime
        }

        self.attribute_map = {
            'invitor_id': 'invitor_id',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email',
            'expires_at': 'expires_at'
        }

        self._invitor_id = invitor_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._expires_at = expires_at

    @classmethod
    def from_dict(cls, dikt) -> 'InvitationCreate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The invitation_create of this InvitationCreate.  # noqa: E501
        :rtype: InvitationCreate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def invitor_id(self) -> str:
        """Gets the invitor_id of this InvitationCreate.

        The user that created the invitation  # noqa: E501

        :return: The invitor_id of this InvitationCreate.
        :rtype: str
        """
        return self._invitor_id

    @invitor_id.setter
    def invitor_id(self, invitor_id: str):
        """Sets the invitor_id of this InvitationCreate.

        The user that created the invitation  # noqa: E501

        :param invitor_id: The invitor_id of this InvitationCreate.
        :type invitor_id: str
        """
        if invitor_id is None:
            raise ValueError("Invalid value for `invitor_id`, must not be `None`")  # noqa: E501

        self._invitor_id = invitor_id

    @property
    def first_name(self) -> str:
        """Gets the first_name of this InvitationCreate.


        :return: The first_name of this InvitationCreate.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this InvitationCreate.


        :param first_name: The first_name of this InvitationCreate.
        :type first_name: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if first_name is not None and len(first_name) > 100:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `100`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this InvitationCreate.


        :return: The last_name of this InvitationCreate.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this InvitationCreate.


        :param last_name: The last_name of this InvitationCreate.
        :type last_name: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501
        if last_name is not None and len(last_name) > 100:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `100`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self) -> str:
        """Gets the email of this InvitationCreate.


        :return: The email of this InvitationCreate.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this InvitationCreate.


        :param email: The email of this InvitationCreate.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def expires_at(self) -> datetime:
        """Gets the expires_at of this InvitationCreate.


        :return: The expires_at of this InvitationCreate.
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at: datetime):
        """Sets the expires_at of this InvitationCreate.


        :param expires_at: The expires_at of this InvitationCreate.
        :type expires_at: datetime
        """

        self._expires_at = expires_at
