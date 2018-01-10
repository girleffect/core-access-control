# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class DomainUpdate(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, parent_id: int=None, name: str=None, description: str=None):
        """
        DomainUpdate - a model defined in Swagger

        :param parent_id: The parent_id of this DomainUpdate.
        :type parent_id: int
        :param name: The name of this DomainUpdate.
        :type name: str
        :param description: The description of this DomainUpdate.
        :type description: str
        """
        self.swagger_types = {
            'parent_id': int,
            'name': str,
            'description': str
        }

        self.attribute_map = {
            'parent_id': 'parent_id',
            'name': 'name',
            'description': 'description'
        }

        self._parent_id = parent_id
        self._name = name
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'DomainUpdate':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The domain_update of this DomainUpdate.
        :rtype: DomainUpdate
        """
        return deserialize_model(dikt, cls)

    @property
    def parent_id(self) -> int:
        """
        Gets the parent_id of this DomainUpdate.

        :return: The parent_id of this DomainUpdate.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id: int):
        """
        Sets the parent_id of this DomainUpdate.

        :param parent_id: The parent_id of this DomainUpdate.
        :type parent_id: int
        """

        self._parent_id = parent_id

    @property
    def name(self) -> str:
        """
        Gets the name of this DomainUpdate.

        :return: The name of this DomainUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this DomainUpdate.

        :param name: The name of this DomainUpdate.
        :type name: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name

    @property
    def description(self) -> str:
        """
        Gets the description of this DomainUpdate.

        :return: The description of this DomainUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """
        Sets the description of this DomainUpdate.

        :param description: The description of this DomainUpdate.
        :type description: str
        """

        self._description = description
