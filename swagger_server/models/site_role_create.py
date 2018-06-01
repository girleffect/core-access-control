# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SiteRoleCreate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, site_id: int=None, role_id: int=None, grant_implicitly: bool=None):  # noqa: E501
        """SiteRoleCreate - a model defined in Swagger

        :param site_id: The site_id of this SiteRoleCreate.  # noqa: E501
        :type site_id: int
        :param role_id: The role_id of this SiteRoleCreate.  # noqa: E501
        :type role_id: int
        :param grant_implicitly: The grant_implicitly of this SiteRoleCreate.  # noqa: E501
        :type grant_implicitly: bool
        """
        self.swagger_types = {
            'site_id': int,
            'role_id': int,
            'grant_implicitly': bool
        }

        self.attribute_map = {
            'site_id': 'site_id',
            'role_id': 'role_id',
            'grant_implicitly': 'grant_implicitly'
        }

        self._site_id = site_id
        self._role_id = role_id
        self._grant_implicitly = grant_implicitly

    @classmethod
    def from_dict(cls, dikt) -> 'SiteRoleCreate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The site_role_create of this SiteRoleCreate.  # noqa: E501
        :rtype: SiteRoleCreate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def site_id(self) -> int:
        """Gets the site_id of this SiteRoleCreate.


        :return: The site_id of this SiteRoleCreate.
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id: int):
        """Sets the site_id of this SiteRoleCreate.


        :param site_id: The site_id of this SiteRoleCreate.
        :type site_id: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def role_id(self) -> int:
        """Gets the role_id of this SiteRoleCreate.


        :return: The role_id of this SiteRoleCreate.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id: int):
        """Sets the role_id of this SiteRoleCreate.


        :param role_id: The role_id of this SiteRoleCreate.
        :type role_id: int
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def grant_implicitly(self) -> bool:
        """Gets the grant_implicitly of this SiteRoleCreate.


        :return: The grant_implicitly of this SiteRoleCreate.
        :rtype: bool
        """
        return self._grant_implicitly

    @grant_implicitly.setter
    def grant_implicitly(self, grant_implicitly: bool):
        """Sets the grant_implicitly of this SiteRoleCreate.


        :param grant_implicitly: The grant_implicitly of this SiteRoleCreate.
        :type grant_implicitly: bool
        """

        self._grant_implicitly = grant_implicitly
