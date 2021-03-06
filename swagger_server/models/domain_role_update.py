# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DomainRoleUpdate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, grant_implicitly: bool=None):  # noqa: E501
        """DomainRoleUpdate - a model defined in Swagger

        :param grant_implicitly: The grant_implicitly of this DomainRoleUpdate.  # noqa: E501
        :type grant_implicitly: bool
        """
        self.swagger_types = {
            'grant_implicitly': bool
        }

        self.attribute_map = {
            'grant_implicitly': 'grant_implicitly'
        }

        self._grant_implicitly = grant_implicitly

    @classmethod
    def from_dict(cls, dikt) -> 'DomainRoleUpdate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The domain_role_update of this DomainRoleUpdate.  # noqa: E501
        :rtype: DomainRoleUpdate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def grant_implicitly(self) -> bool:
        """Gets the grant_implicitly of this DomainRoleUpdate.


        :return: The grant_implicitly of this DomainRoleUpdate.
        :rtype: bool
        """
        return self._grant_implicitly

    @grant_implicitly.setter
    def grant_implicitly(self, grant_implicitly: bool):
        """Sets the grant_implicitly of this DomainRoleUpdate.


        :param grant_implicitly: The grant_implicitly of this DomainRoleUpdate.
        :type grant_implicitly: bool
        """

        self._grant_implicitly = grant_implicitly
