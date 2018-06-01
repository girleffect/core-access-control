# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ResourcePermission(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, resource_id: int=None, permission_id: int=None):  # noqa: E501
        """ResourcePermission - a model defined in Swagger

        :param resource_id: The resource_id of this ResourcePermission.  # noqa: E501
        :type resource_id: int
        :param permission_id: The permission_id of this ResourcePermission.  # noqa: E501
        :type permission_id: int
        """
        self.swagger_types = {
            'resource_id': int,
            'permission_id': int
        }

        self.attribute_map = {
            'resource_id': 'resource_id',
            'permission_id': 'permission_id'
        }

        self._resource_id = resource_id
        self._permission_id = permission_id

    @classmethod
    def from_dict(cls, dikt) -> 'ResourcePermission':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The resource_permission of this ResourcePermission.  # noqa: E501
        :rtype: ResourcePermission
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resource_id(self) -> int:
        """Gets the resource_id of this ResourcePermission.


        :return: The resource_id of this ResourcePermission.
        :rtype: int
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id: int):
        """Sets the resource_id of this ResourcePermission.


        :param resource_id: The resource_id of this ResourcePermission.
        :type resource_id: int
        """
        if resource_id is None:
            raise ValueError("Invalid value for `resource_id`, must not be `None`")  # noqa: E501

        self._resource_id = resource_id

    @property
    def permission_id(self) -> int:
        """Gets the permission_id of this ResourcePermission.


        :return: The permission_id of this ResourcePermission.
        :rtype: int
        """
        return self._permission_id

    @permission_id.setter
    def permission_id(self, permission_id: int):
        """Sets the permission_id of this ResourcePermission.


        :param permission_id: The permission_id of this ResourcePermission.
        :type permission_id: int
        """
        if permission_id is None:
            raise ValueError("Invalid value for `permission_id`, must not be `None`")  # noqa: E501

        self._permission_id = permission_id
