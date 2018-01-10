# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class InvitationDomainRole(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, invitation_id: str=None, domain_id: int=None, role_id: int=None, created_at: datetime=None, updated_at: datetime=None):
        """
        InvitationDomainRole - a model defined in Swagger

        :param invitation_id: The invitation_id of this InvitationDomainRole.
        :type invitation_id: str
        :param domain_id: The domain_id of this InvitationDomainRole.
        :type domain_id: int
        :param role_id: The role_id of this InvitationDomainRole.
        :type role_id: int
        :param created_at: The created_at of this InvitationDomainRole.
        :type created_at: datetime
        :param updated_at: The updated_at of this InvitationDomainRole.
        :type updated_at: datetime
        """
        self.swagger_types = {
            'invitation_id': str,
            'domain_id': int,
            'role_id': int,
            'created_at': datetime,
            'updated_at': datetime
        }

        self.attribute_map = {
            'invitation_id': 'invitation_id',
            'domain_id': 'domain_id',
            'role_id': 'role_id',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._invitation_id = invitation_id
        self._domain_id = domain_id
        self._role_id = role_id
        self._created_at = created_at
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt) -> 'InvitationDomainRole':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The invitation_domain_role of this InvitationDomainRole.
        :rtype: InvitationDomainRole
        """
        return deserialize_model(dikt, cls)

    @property
    def invitation_id(self) -> str:
        """
        Gets the invitation_id of this InvitationDomainRole.

        :return: The invitation_id of this InvitationDomainRole.
        :rtype: str
        """
        return self._invitation_id

    @invitation_id.setter
    def invitation_id(self, invitation_id: str):
        """
        Sets the invitation_id of this InvitationDomainRole.

        :param invitation_id: The invitation_id of this InvitationDomainRole.
        :type invitation_id: str
        """
        if invitation_id is None:
            raise ValueError("Invalid value for `invitation_id`, must not be `None`")

        self._invitation_id = invitation_id

    @property
    def domain_id(self) -> int:
        """
        Gets the domain_id of this InvitationDomainRole.

        :return: The domain_id of this InvitationDomainRole.
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id: int):
        """
        Sets the domain_id of this InvitationDomainRole.

        :param domain_id: The domain_id of this InvitationDomainRole.
        :type domain_id: int
        """
        if domain_id is None:
            raise ValueError("Invalid value for `domain_id`, must not be `None`")

        self._domain_id = domain_id

    @property
    def role_id(self) -> int:
        """
        Gets the role_id of this InvitationDomainRole.

        :return: The role_id of this InvitationDomainRole.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id: int):
        """
        Sets the role_id of this InvitationDomainRole.

        :param role_id: The role_id of this InvitationDomainRole.
        :type role_id: int
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")

        self._role_id = role_id

    @property
    def created_at(self) -> datetime:
        """
        Gets the created_at of this InvitationDomainRole.

        :return: The created_at of this InvitationDomainRole.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: datetime):
        """
        Sets the created_at of this InvitationDomainRole.

        :param created_at: The created_at of this InvitationDomainRole.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def updated_at(self) -> datetime:
        """
        Gets the updated_at of this InvitationDomainRole.

        :return: The updated_at of this InvitationDomainRole.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        """
        Sets the updated_at of this InvitationDomainRole.

        :param updated_at: The updated_at of this InvitationDomainRole.
        :type updated_at: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at
