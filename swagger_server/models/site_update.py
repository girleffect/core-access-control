# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SiteUpdate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, client_id: int=None, domain_id: int=None, name: str=None, description: str=None, is_active: bool=None, deletion_method_id: int=None, deletion_method_data: object=None):  # noqa: E501
        """SiteUpdate - a model defined in Swagger

        :param client_id: The client_id of this SiteUpdate.  # noqa: E501
        :type client_id: int
        :param domain_id: The domain_id of this SiteUpdate.  # noqa: E501
        :type domain_id: int
        :param name: The name of this SiteUpdate.  # noqa: E501
        :type name: str
        :param description: The description of this SiteUpdate.  # noqa: E501
        :type description: str
        :param is_active: The is_active of this SiteUpdate.  # noqa: E501
        :type is_active: bool
        :param deletion_method_id: The deletion_method_id of this SiteUpdate.  # noqa: E501
        :type deletion_method_id: int
        :param deletion_method_data: The deletion_method_data of this SiteUpdate.  # noqa: E501
        :type deletion_method_data: object
        """
        self.swagger_types = {
            'client_id': int,
            'domain_id': int,
            'name': str,
            'description': str,
            'is_active': bool,
            'deletion_method_id': int,
            'deletion_method_data': object
        }

        self.attribute_map = {
            'client_id': 'client_id',
            'domain_id': 'domain_id',
            'name': 'name',
            'description': 'description',
            'is_active': 'is_active',
            'deletion_method_id': 'deletion_method_id',
            'deletion_method_data': 'deletion_method_data'
        }

        self._client_id = client_id
        self._domain_id = domain_id
        self._name = name
        self._description = description
        self._is_active = is_active
        self._deletion_method_id = deletion_method_id
        self._deletion_method_data = deletion_method_data

    @classmethod
    def from_dict(cls, dikt) -> 'SiteUpdate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The site_update of this SiteUpdate.  # noqa: E501
        :rtype: SiteUpdate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client_id(self) -> int:
        """Gets the client_id of this SiteUpdate.


        :return: The client_id of this SiteUpdate.
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: int):
        """Sets the client_id of this SiteUpdate.


        :param client_id: The client_id of this SiteUpdate.
        :type client_id: int
        """

        self._client_id = client_id

    @property
    def domain_id(self) -> int:
        """Gets the domain_id of this SiteUpdate.


        :return: The domain_id of this SiteUpdate.
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id: int):
        """Sets the domain_id of this SiteUpdate.


        :param domain_id: The domain_id of this SiteUpdate.
        :type domain_id: int
        """

        self._domain_id = domain_id

    @property
    def name(self) -> str:
        """Gets the name of this SiteUpdate.


        :return: The name of this SiteUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this SiteUpdate.


        :param name: The name of this SiteUpdate.
        :type name: str
        """
        if name is not None and len(name) > 30:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `30`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this SiteUpdate.


        :return: The description of this SiteUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this SiteUpdate.


        :param description: The description of this SiteUpdate.
        :type description: str
        """

        self._description = description

    @property
    def is_active(self) -> bool:
        """Gets the is_active of this SiteUpdate.


        :return: The is_active of this SiteUpdate.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active: bool):
        """Sets the is_active of this SiteUpdate.


        :param is_active: The is_active of this SiteUpdate.
        :type is_active: bool
        """

        self._is_active = is_active

    @property
    def deletion_method_id(self) -> int:
        """Gets the deletion_method_id of this SiteUpdate.


        :return: The deletion_method_id of this SiteUpdate.
        :rtype: int
        """
        return self._deletion_method_id

    @deletion_method_id.setter
    def deletion_method_id(self, deletion_method_id: int):
        """Sets the deletion_method_id of this SiteUpdate.


        :param deletion_method_id: The deletion_method_id of this SiteUpdate.
        :type deletion_method_id: int
        """

        self._deletion_method_id = deletion_method_id

    @property
    def deletion_method_data(self) -> object:
        """Gets the deletion_method_data of this SiteUpdate.


        :return: The deletion_method_data of this SiteUpdate.
        :rtype: object
        """
        return self._deletion_method_data

    @deletion_method_data.setter
    def deletion_method_data(self, deletion_method_data: object):
        """Sets the deletion_method_data of this SiteUpdate.


        :param deletion_method_data: The deletion_method_data of this SiteUpdate.
        :type deletion_method_data: object
        """

        self._deletion_method_data = deletion_method_data
