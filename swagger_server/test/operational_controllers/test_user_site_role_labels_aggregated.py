# coding: utf-8

from __future__ import absolute_import
import random
import uuid

from ge_core_shared import db_actions, decorators
from flask import json

from project.settings import API_KEY_HEADER
from swagger_server.models.user_site_role import UserSiteRole  # noqa: E501
from swagger_server.models.site_role import SiteRole  # noqa: E501
from swagger_server.models.domain import Domain  # noqa: E501
from swagger_server.models.role import Role  # noqa: E501
from swagger_server.models.site import Site  # noqa: E501
from swagger_server.models.site_create import SiteCreate  # noqa: E501
from swagger_server.test import BaseTestCase, db_create_entry


class TestOperationalController(BaseTestCase):

    @decorators.db_exception
    def setUp(self):
        super().setUp()
        self.domain_data = {
            "name": ("%s" % uuid.uuid1())[:30],
            "description": "a super cool test domain",
        }
        self.domain_model = db_actions.crud(
            model="Domain",
            api_model=Domain,
            data=self.domain_data,
            action="create"
        )
        site_data = {
            "name": ("%s" % uuid.uuid1())[:30],
            "domain_id": self.domain_model.id,
            "description": "a super cool test site",
            "client_id": 0,
            "is_active": True,
        }
        self.site_model = db_create_entry(
            model="Site",
            data=site_data,
        )
        self.roles = []

        # create a bunch of roles.
        for index in range(1, random.randint(5, 20)):
            role_data = {
                "label": ("%s" % uuid.uuid1())[:30],
                "description": "user_site_role to create",
            }
            role_model = db_actions.crud(
                model="Role",
                api_model=Role,
                data=role_data,
                action="create"
            )
            self.roles.append(role_model)

        self.user_id = "%s" % uuid.uuid1()
        for role in self.roles:
            site_role_data = {
                "role_id": role.id,
                "site_id": self.site_model.id,
            }
            site_role_model = db_actions.crud(
                model="SiteRole",
                api_model=SiteRole,
                data=site_role_data,
                action="create"
            )

            user_site_role_data = {
                "role_id": role.id,
                "site_id": self.site_model.id,
                "user_id": self.user_id,
            }
            user_site_role_model = db_actions.crud(
                model="UserSiteRole",
                api_model=UserSiteRole,
                data=user_site_role_data,
                action="create"
            )

        self.headers = {API_KEY_HEADER: "test-api-key"}

    def test_get_user_site_role_labels_aggregated(self):
        """Test case for get_user_site_role_labels_aggregated
        """
        response = self.client.open(
            "/api/v1/ops/user_site_role_labels_aggregated/{user_id}/{site_id}".format(
                user_id=self.user_id, site_id=self.site_model.id
        ),
            method='GET', headers=self.headers)
        r_data = json.loads(response.data)
        self.assertEqual(len(r_data["roles"]), len(self.roles))
        for role in self.roles:
            self.assertIn(role.label, r_data["roles"])
        self.assertEqual(self.site_model.id, r_data["site_id"])
        self.assertEqual(self.user_id, r_data["user_id"])


if __name__ == '__main__':
    import unittest
    unittest.main()
