# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Credentials(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, site_id: int=None, account_id: str=None, account_secret: str=None, description: str=None, created_at: datetime=None, updated_at: datetime=None):  # noqa: E501
        """Credentials - a model defined in Swagger

        :param id: The id of this Credentials.  # noqa: E501
        :type id: int
        :param site_id: The site_id of this Credentials.  # noqa: E501
        :type site_id: int
        :param account_id: The account_id of this Credentials.  # noqa: E501
        :type account_id: str
        :param account_secret: The account_secret of this Credentials.  # noqa: E501
        :type account_secret: str
        :param description: The description of this Credentials.  # noqa: E501
        :type description: str
        :param created_at: The created_at of this Credentials.  # noqa: E501
        :type created_at: datetime
        :param updated_at: The updated_at of this Credentials.  # noqa: E501
        :type updated_at: datetime
        """
        self.swagger_types = {
            'id': int,
            'site_id': int,
            'account_id': str,
            'account_secret': str,
            'description': str,
            'created_at': datetime,
            'updated_at': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'site_id': 'site_id',
            'account_id': 'account_id',
            'account_secret': 'account_secret',
            'description': 'description',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._id = id
        self._site_id = site_id
        self._account_id = account_id
        self._account_secret = account_secret
        self._description = description
        self._created_at = created_at
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt) -> 'Credentials':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The credentials of this Credentials.  # noqa: E501
        :rtype: Credentials
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Credentials.


        :return: The id of this Credentials.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Credentials.


        :param id: The id of this Credentials.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def site_id(self) -> int:
        """Gets the site_id of this Credentials.


        :return: The site_id of this Credentials.
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id: int):
        """Sets the site_id of this Credentials.


        :param site_id: The site_id of this Credentials.
        :type site_id: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def account_id(self) -> str:
        """Gets the account_id of this Credentials.


        :return: The account_id of this Credentials.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id: str):
        """Sets the account_id of this Credentials.


        :param account_id: The account_id of this Credentials.
        :type account_id: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501
        if account_id is not None and len(account_id) > 256:
            raise ValueError("Invalid value for `account_id`, length must be less than or equal to `256`")  # noqa: E501
        if account_id is not None and len(account_id) < 32:
            raise ValueError("Invalid value for `account_id`, length must be greater than or equal to `32`")  # noqa: E501

        self._account_id = account_id

    @property
    def account_secret(self) -> str:
        """Gets the account_secret of this Credentials.


        :return: The account_secret of this Credentials.
        :rtype: str
        """
        return self._account_secret

    @account_secret.setter
    def account_secret(self, account_secret: str):
        """Sets the account_secret of this Credentials.


        :param account_secret: The account_secret of this Credentials.
        :type account_secret: str
        """
        if account_secret is None:
            raise ValueError("Invalid value for `account_secret`, must not be `None`")  # noqa: E501
        if account_secret is not None and len(account_secret) > 256:
            raise ValueError("Invalid value for `account_secret`, length must be less than or equal to `256`")  # noqa: E501
        if account_secret is not None and len(account_secret) < 32:
            raise ValueError("Invalid value for `account_secret`, length must be greater than or equal to `32`")  # noqa: E501

        self._account_secret = account_secret

    @property
    def description(self) -> str:
        """Gets the description of this Credentials.


        :return: The description of this Credentials.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Credentials.


        :param description: The description of this Credentials.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def created_at(self) -> datetime:
        """Gets the created_at of this Credentials.


        :return: The created_at of this Credentials.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """Sets the created_at of this Credentials.


        :param created_at: The created_at of this Credentials.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self) -> datetime:
        """Gets the updated_at of this Credentials.


        :return: The updated_at of this Credentials.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        """Sets the updated_at of this Credentials.


        :param updated_at: The updated_at of this Credentials.
        :type updated_at: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at
