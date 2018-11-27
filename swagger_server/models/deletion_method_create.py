# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DeletionMethodCreate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, label: str=None, data_schema: object=None, description: str=None):  # noqa: E501
        """DeletionMethodCreate - a model defined in Swagger

        :param label: The label of this DeletionMethodCreate.  # noqa: E501
        :type label: str
        :param data_schema: The data_schema of this DeletionMethodCreate.  # noqa: E501
        :type data_schema: object
        :param description: The description of this DeletionMethodCreate.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'label': str,
            'data_schema': object,
            'description': str
        }

        self.attribute_map = {
            'label': 'label',
            'data_schema': 'data_schema',
            'description': 'description'
        }

        self._label = label
        self._data_schema = data_schema
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'DeletionMethodCreate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The deletion_method_create of this DeletionMethodCreate.  # noqa: E501
        :rtype: DeletionMethodCreate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def label(self) -> str:
        """Gets the label of this DeletionMethodCreate.


        :return: The label of this DeletionMethodCreate.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label: str):
        """Sets the label of this DeletionMethodCreate.


        :param label: The label of this DeletionMethodCreate.
        :type label: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501
        if label is not None and len(label) > 100:
            raise ValueError("Invalid value for `label`, length must be less than or equal to `100`")  # noqa: E501

        self._label = label

    @property
    def data_schema(self) -> object:
        """Gets the data_schema of this DeletionMethodCreate.


        :return: The data_schema of this DeletionMethodCreate.
        :rtype: object
        """
        return self._data_schema

    @data_schema.setter
    def data_schema(self, data_schema: object):
        """Sets the data_schema of this DeletionMethodCreate.


        :param data_schema: The data_schema of this DeletionMethodCreate.
        :type data_schema: object
        """
        if data_schema is None:
            raise ValueError("Invalid value for `data_schema`, must not be `None`")  # noqa: E501

        self._data_schema = data_schema

    @property
    def description(self) -> str:
        """Gets the description of this DeletionMethodCreate.


        :return: The description of this DeletionMethodCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this DeletionMethodCreate.


        :param description: The description of this DeletionMethodCreate.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description
