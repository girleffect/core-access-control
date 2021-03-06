# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SiteAndDomainRoles(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, site_id: int=None, roles_map: Dict[str, List[int]]=None):  # noqa: E501
        """SiteAndDomainRoles - a model defined in Swagger

        :param site_id: The site_id of this SiteAndDomainRoles.  # noqa: E501
        :type site_id: int
        :param roles_map: The roles_map of this SiteAndDomainRoles.  # noqa: E501
        :type roles_map: Dict[str, List[int]]
        """
        self.swagger_types = {
            'site_id': int,
            'roles_map': Dict[str, List[int]]
        }

        self.attribute_map = {
            'site_id': 'site_id',
            'roles_map': 'roles_map'
        }

        self._site_id = site_id
        self._roles_map = roles_map

    @classmethod
    def from_dict(cls, dikt) -> 'SiteAndDomainRoles':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The site_and_domain_roles of this SiteAndDomainRoles.  # noqa: E501
        :rtype: SiteAndDomainRoles
        """
        return util.deserialize_model(dikt, cls)

    @property
    def site_id(self) -> int:
        """Gets the site_id of this SiteAndDomainRoles.

        The site for which the request was made.  # noqa: E501

        :return: The site_id of this SiteAndDomainRoles.
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id: int):
        """Sets the site_id of this SiteAndDomainRoles.

        The site for which the request was made.  # noqa: E501

        :param site_id: The site_id of this SiteAndDomainRoles.
        :type site_id: int
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

    @property
    def roles_map(self) -> Dict[str, List[int]]:
        """Gets the roles_map of this SiteAndDomainRoles.

        A dictionary where the keys are site and domain ids prefixed with `s:` and `d:`, respectively and the values are lists of role ids.  # noqa: E501

        :return: The roles_map of this SiteAndDomainRoles.
        :rtype: Dict[str, List[int]]
        """
        return self._roles_map

    @roles_map.setter
    def roles_map(self, roles_map: Dict[str, List[int]]):
        """Sets the roles_map of this SiteAndDomainRoles.

        A dictionary where the keys are site and domain ids prefixed with `s:` and `d:`, respectively and the values are lists of role ids.  # noqa: E501

        :param roles_map: The roles_map of this SiteAndDomainRoles.
        :type roles_map: Dict[str, List[int]]
        """
        if roles_map is None:
            raise ValueError("Invalid value for `roles_map`, must not be `None`")  # noqa: E501

        self._roles_map = roles_map
