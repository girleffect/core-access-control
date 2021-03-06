# coding: utf-8

from __future__ import absolute_import
import random
import uuid

import werkzeug
from flask import json

from project.settings import API_KEY_HEADER
from swagger_server.models.site_role import SiteRole  # noqa: E501
from swagger_server.models.site_role_update import SiteRoleUpdate  # noqa: E501
from swagger_server.models.site_role_create import SiteRoleCreate  # noqa: E501
from swagger_server.models.domain import Domain  # noqa: E501
from swagger_server.models.role import Role  # noqa: E501
from swagger_server.models.site import Site  # noqa: E501
from swagger_server.models.site_create import SiteCreate  # noqa: E501
from swagger_server.test import BaseTestCase, db_create_entry
from ge_core_shared import db_actions, decorators


class SiteRoleTestCase(BaseTestCase):

    @decorators.db_exception
    def setUp(self):
        super().setUp()
        self.role_data = {
            "label": ("%s" % uuid.uuid1())[:30],
            "description": "site_role to create",
        }
        self.role_model = db_actions.crud(
            model="Role",
            api_model=Role,
            data=self.role_data,
            action="create"
        )
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
        self.site_data = {
            "name": ("%s" % uuid.uuid1())[:30],
            "domain_id": self.domain_model.id,
            "description": "a super cool test site",
            "client_id": uuid.uuid1().int>>97,
            "is_active": True,
        }
        self.site_model = db_create_entry(
            model="Site",
            data=self.site_data,
        )

        self.site_role_data = {
            "role_id": self.role_model.id,
            "site_id": self.site_model.id,
        }
        self.site_role_model = db_actions.crud(
            model="SiteRole",
            api_model=SiteRole,
            data=self.site_role_data,
            action="create"
        )

        self.headers = {API_KEY_HEADER: "test-api-key"}

    def test_site_role_create(self):
        """Test case for site_role_create
        """
        role_data = {
            "label": ("%s" % uuid.uuid1())[:30],
            "description": "site_role to create",
        }
        role_model = db_actions.crud(
            model="Role",
            api_model=Role,
            data=role_data,
            action="create"
        )
        domain_data = {
            "name": ("%s" % uuid.uuid1())[:30],
            "description": "a super cool test domain",
        }
        domain_model = db_actions.crud(
            model="Domain",
            api_model=Domain,
            data=domain_data,
            action="create"
        )
        site_data = {
            "name": ("%s" % uuid.uuid1())[:30],
            "domain_id": domain_model.id,
            "description": "a super cool test site",
            "client_id": uuid.uuid1().int>>97,
            "is_active": True,
        }
        site_model = db_create_entry(
            model="Site",
            data=site_data,
        )

        data = SiteRoleCreate(**{
            "role_id": role_model.id,
            "site_id": site_model.id,
            "grant_implicitly": True,
        })
        response = self.client.open(
            '/api/v1/siteroles',
            method='POST',
            data=json.dumps(data),
            content_type='application/json',
            headers=self.headers)
        r_data = json.loads(response.data)
        self.assertEqual(r_data["role_id"], data.role_id)
        self.assertEqual(r_data["site_id"], data.site_id)

    def test_site_role_read(self):
        """Test case for site_role_read
        """
        response = self.client.open(
            '/api/v1/siteroles/{site_id}/{role_id}'.format(
                site_id=self.site_role_model.site_id,
                role_id=self.site_role_model.role_id,
            ),
            method='GET', headers=self.headers)
        r_data = json.loads(response.data)
        self.assertEqual(r_data["role_id"], self.site_role_model.role_id)
        self.assertEqual(r_data["site_id"], self.site_role_model.site_id)

    def test_site_role_delete(self):
        """Test case for site_role_delete
        """
        role_data = {
            "label": ("%s" % uuid.uuid1())[:30],
            "description": "site_role to create",
        }
        role_model = db_actions.crud(
            model="Role",
            api_model=Role,
            data=role_data,
            action="create"
        )
        domain_data = {
            "name": ("%s" % uuid.uuid1())[:30],
            "description": "site_role to create",
        }
        domain_model = db_actions.crud(
            model="Domain",
            api_model=Domain,
            data=domain_data,
            action="create"
        )
        site_data = {
            "name": ("%s" % uuid.uuid1())[:30],
            "domain_id": domain_model.id,
            "description": "a super cool test site",
            "client_id": uuid.uuid1().int>>97,
            "is_active": True,
        }
        site_model = db_create_entry(
            model="Site",
            data=site_data,
        )

        site_role_data = {
            "role_id": role_model.id,
            "site_id": site_model.id,
        }
        model = db_actions.crud(
            model="SiteRole",
            api_model=SiteRole,
            data=site_role_data,
            action="create"
        )
        response = self.client.open(
            '/api/v1/siteroles/{site_id}/{role_id}'.format(
                site_id=model.site_id,
                role_id=model.role_id,
            ),
            method='DELETE', headers=self.headers)

        # Little crude. Raise an error if the object actually still exists else
        # pass after the 404 error.
        with self.assertRaises(werkzeug.exceptions.NotFound):
            db_actions.crud(
                model="SiteRole",
                api_model=SiteRole,
                action="read",
                query={
                    "role_id": model.role_id,
                    "site_id": model.site_id,
                }
            )

    def test_site_role_list(self):
        """Test case for site_role_list
        """
        objects = []
        role_data = {
            "label": ("%s" % uuid.uuid1())[:30],
            "description": "site_role to create",
        }
        role_model = db_actions.crud(
            model="Role",
            api_model=Role,
            data=role_data,
            action="create"
        )
        for index in range(1, random.randint(5, 20)):
            domain_data = {
                "name": ("%s" % uuid.uuid1())[:30],
                "description": "site_role to create",
            }
            domain_model = db_actions.crud(
                model="Domain",
                api_model=Domain,
                data=domain_data,
                action="create"
            )
            site_data = {
                "name": ("%s" % uuid.uuid1())[:30],
                "domain_id": domain_model.id,
                "description": "a super cool test site",
                "client_id": uuid.uuid1().int>>97,
                "is_active": True,
            }
            site_model = db_create_entry(
                model="Site",
                data=site_data,
            )

            site_role_data = {
                "role_id": role_model.id,
                "site_id": site_model.id,
            }
            objects.append(db_actions.crud(
                model="SiteRole",
                api_model=SiteRole,
                data=site_role_data,
                action="create"
            ))
        query_string = [#('offset', 0),
                        ('role_id', role_model.id),
        ]
        response = self.client.open(
            '/api/v1/siteroles',
            method='GET',
            query_string=query_string,
            headers=self.headers)
        r_data = json.loads(response.data)
        self.assertEqual(len(r_data), len(objects))
        self.assertEqual(int(response.headers["X-Total-Count"]), len(objects))
        query_string = [#('offset', 0),
                        ('limit', 2),
                        ('role_id', role_model.id),
        ]
        response = self.client.open(
            '/api/v1/siteroles',
            method='GET',
            query_string=query_string,
            headers=self.headers)
        r_data = json.loads(response.data)
        self.assertEqual(len(r_data), 2)
        self.assertEqual(int(response.headers["X-Total-Count"]), len(objects))

    def test_site_role_update(self):
        """Test case for site_role_update
        """
        role_data = {
            "label": ("%s" % uuid.uuid1())[:30],
            "description": "site_role to create",
        }
        role_model = db_actions.crud(
            model="Role",
            api_model=Role,
            data=role_data,
            action="create"
        )
        domain_data = {
            "name": ("%s" % uuid.uuid1())[:30],
            "description": "site_role to create",
        }
        domain_model = db_actions.crud(
            model="Domain",
            api_model=Domain,
            data=domain_data,
            action="create"
        )
        site_data = {
            "name": ("%s" % uuid.uuid1())[:30],
            "domain_id": domain_model.id,
            "description": "a super cool test site",
            "client_id": uuid.uuid1().int>>97,
            "is_active": True,
        }
        site_model = db_create_entry(
            model="Site",
            data=site_data,
        )
        site_role_data = {
            "role_id": role_model.id,
            "site_id": site_model.id,
            "grant_implicitly": True
        }
        site_role_model = db_actions.crud(
            model="SiteRole",
            api_model=SiteRole,
            data=site_role_data,
            action="create"
        )

        # Change grant on the model.
        data = {
            "grant_implicitly": False
        }
        data = SiteRoleUpdate(
            **data
        )
        response = self.client.open(
            '/api/v1/siteroles/{site_id}/{role_id}'.format(
                site_id=site_role_model.site_id,
                role_id=site_role_model.role_id,
            ),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json',
            headers=self.headers)
        r_data = json.loads(response.data)
        updated_entry = db_actions.crud(
            model="SiteRole",
            api_model=SiteRole,
            action="read",
            query={
                "role_id": site_role_model.role_id,
                "site_id": site_role_model.site_id,
            }
        )
        self.assertEqual(r_data["grant_implicitly"], updated_entry.grant_implicitly)
