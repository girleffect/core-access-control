# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SiteCreate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, client_id: str=None, domain_id: int=None, description: str=None, is_active: bool=None):  # noqa: E501
        """SiteCreate - a model defined in Swagger

        :param name: The name of this SiteCreate.  # noqa: E501
        :type name: str
        :param client_id: The client_id of this SiteCreate.  # noqa: E501
        :type client_id: str
        :param domain_id: The domain_id of this SiteCreate.  # noqa: E501
        :type domain_id: int
        :param description: The description of this SiteCreate.  # noqa: E501
        :type description: str
        :param is_active: The is_active of this SiteCreate.  # noqa: E501
        :type is_active: bool
        """
        self.swagger_types = {
            'name': str,
            'client_id': str,
            'domain_id': int,
            'description': str,
            'is_active': bool
        }

        self.attribute_map = {
            'name': 'name',
            'client_id': 'client_id',
            'domain_id': 'domain_id',
            'description': 'description',
            'is_active': 'is_active'
        }

        self._name = name
        self._client_id = client_id
        self._domain_id = domain_id
        self._description = description
        self._is_active = is_active

    @classmethod
    def from_dict(cls, dikt) -> 'SiteCreate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The site_create of this SiteCreate.  # noqa: E501
        :rtype: SiteCreate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this SiteCreate.


        :return: The name of this SiteCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SiteCreate.


        :param name: The name of this SiteCreate.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 30:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `30`")  # noqa: E501

        self._name = name

    @property
    def client_id(self) -> str:
        """Gets the client_id of this SiteCreate.


        :return: The client_id of this SiteCreate.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: str):
        """Sets the client_id of this SiteCreate.


        :param client_id: The client_id of this SiteCreate.
        :type client_id: str
        """

        self._client_id = client_id

    @property
    def domain_id(self) -> int:
        """Gets the domain_id of this SiteCreate.


        :return: The domain_id of this SiteCreate.
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id: int):
        """Sets the domain_id of this SiteCreate.


        :param domain_id: The domain_id of this SiteCreate.
        :type domain_id: int
        """
        if domain_id is None:
            raise ValueError("Invalid value for `domain_id`, must not be `None`")  # noqa: E501

        self._domain_id = domain_id

    @property
    def description(self) -> str:
        """Gets the description of this SiteCreate.


        :return: The description of this SiteCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this SiteCreate.


        :param description: The description of this SiteCreate.
        :type description: str
        """

        self._description = description

    @property
    def is_active(self) -> bool:
        """Gets the is_active of this SiteCreate.


        :return: The is_active of this SiteCreate.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active: bool):
        """Sets the is_active of this SiteCreate.


        :param is_active: The is_active of this SiteCreate.
        :type is_active: bool
        """

        self._is_active = is_active
