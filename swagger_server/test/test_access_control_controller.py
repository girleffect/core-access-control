# coding: utf-8

from __future__ import absolute_import

import datetime
import uuid
import werkzeug

from flask import json
from six import BytesIO

from swagger_server.models.all_user_roles import AllUserRoles  # noqa: E501
from swagger_server.models.domain import Domain  # noqa: E501
from swagger_server.models.domain_role import DomainRole  # noqa: E501
from swagger_server.models.domain_role_update import DomainRoleUpdate  # noqa: E501
from swagger_server.models.domain_update import DomainUpdate  # noqa: E501
from swagger_server.models.invitation import Invitation  # noqa: E501
from swagger_server.models.invitation_domain_role import InvitationDomainRole  # noqa: E501
from swagger_server.models.invitation_site_role import InvitationSiteRole  # noqa: E501
from swagger_server.models.invitation_update import InvitationUpdate  # noqa: E501
from swagger_server.models.permission import Permission  # noqa: E501
from swagger_server.models.permission_update import PermissionUpdate  # noqa: E501
from swagger_server.models.resource import Resource  # noqa: E501
from swagger_server.models.resource_update import ResourceUpdate  # noqa: E501
from swagger_server.models.role import Role  # noqa: E501
from swagger_server.models.role_resource_permission import RoleResourcePermission  # noqa: E501
from swagger_server.models.role_update import RoleUpdate  # noqa: E501
from swagger_server.models.site import Site  # noqa: E501
from swagger_server.models.site_role import SiteRole  # noqa: E501
from swagger_server.models.site_role_update import SiteRoleUpdate  # noqa: E501
from swagger_server.models.site_update import SiteUpdate  # noqa: E501
from swagger_server.models.user_domain_role import UserDomainRole  # noqa: E501
from swagger_server.models.user_site_role import UserSiteRole  # noqa: E501
from swagger_server.test import BaseTestCase

from core_access_control import models, db_actions
class TestAccessControlRead(BaseTestCase):

    def setUp(self):
        self.domain_data = {
            "name": ("%s" % uuid.uuid4())[:30],
            "description": "a super cool test domain",
        }
        self.domain_model = db_actions.crud(
            model="Domain",
            api_model=Domain,
            data=self.domain_data,
            action="create"
        )

    def test_domain_create(self):
        """Test case for domainrole_create
        """
        data = Domain(**{
            "name": ("%s" % uuid.uuid4())[:30],
            "description": "Domain to create",
        })
        response = self.client.open(
            '/api/v1/domains/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        r_data = json.loads(response.data)
        self.assertEqual(r_data["name"], data.name)
        self.assertEqual(r_data["description"], data.description)


    def test_domain_read(self):
        """Test case for domain_read
        """
        response = self.client.open(
            '/api/v1/domains/{domain_id}/'.format(domain_id=self.domain_model.id),
            method='GET')
        r_data = json.loads(response.data)
        self.assertEqual(r_data["name"], self.domain_model.name)
        self.assertEqual(r_data["description"], self.domain_model.description)
        self.assertEqual(r_data["id"], self.domain_model.id)

    def test_domain_delete(self):
        """Test case for domain_delete
        """
        data = {
            "name": ("%s" % uuid.uuid4())[:30],
            "description": "Domain to delete",
        }
        model = db_actions.crud(
            model="Domain",
            api_model=Domain,
            data=data,
            action="create"
        )
        response = self.client.open(
            '/api/v1/domains/{domain_id}/'.format(domain_id=model.id),
            method='DELETE')

        # Little crude. Raise an error if the object actually still exists else
        # pass after the 404 error.
        try:
            db_actions.crud(
                model="Domain",
                api_model=Domain,
                action="read",
                query={"id": model.id}
            )
            raise Exception
        except werkzeug.exceptions.NotFound:
            pass

    def test_domain_list(self):
        """Test case for domain_list
        """
        data = [
            {
                "name": ("%s" % uuid.uuid4())[:30],
                "description": "Domain list 1",
            },
            {
                "name": ("%s" % uuid.uuid4())[:30],
                "description": "Domain list 2",
            },
            {
                "name": ("%s" % uuid.uuid4())[:30],
                "description": "Domain list 3",
            },
        ]

        objects = []
        for item in data:
            objects.append(db_actions.crud(
                model="Domain",
                api_model=Domain,
                data=item,
                action="create"
            ))
        query_string = [('offset', 1),
                        #('limit', ),
                        ('domain_ids', objects[2].id)]
        response = self.client.open(
            '/api/v1/domains/',
            method='GET',
            query_string=query_string)
        r_data = json.loads(response.data)
