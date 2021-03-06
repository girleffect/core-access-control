# coding: utf-8

from __future__ import absolute_import
import random
import uuid

import werkzeug
from flask import json

from project.settings import API_KEY_HEADER
from swagger_server.models.permission import Permission  # noqa: E501
from swagger_server.models.permission_update import PermissionUpdate  # noqa: E501
from swagger_server.test import BaseTestCase
from ge_core_shared import db_actions, decorators


class PermissionTestCase(BaseTestCase):

    @decorators.db_exception
    def setUp(self):
        super().setUp()
        self.permission_data = {
            "name": ("%s" % uuid.uuid1())[:30],
            "description": "a super cool test permission",
        }
        self.permission_model = db_actions.crud(
            model="Permission",
            api_model=Permission,
            data=self.permission_data,
            action="create"
        )

        self.headers = {API_KEY_HEADER: "test-api-key"}

    def test_permission_create(self):
        """Test case for permission_create
        """
        data = Permission(**{
            "name": ("%s" % uuid.uuid1())[:30],
            "description": "permission to create",
        })
        response = self.client.open(
            '/api/v1/permissions',
            method='POST',
            data=json.dumps(data),
            content_type='application/json',
            headers=self.headers)
        r_data = json.loads(response.data)
        self.assertEqual(r_data["name"], data.name)
        self.assertEqual(r_data["description"], data.description)

    def test_permission_read(self):
        """Test case for permission_read
        """
        response = self.client.open(
            '/api/v1/permissions/{permission_id}'.format(permission_id=self.permission_model.id),
            method='GET', headers=self.headers)
        r_data = json.loads(response.data)
        self.assertEqual(r_data["name"], self.permission_model.name)
        self.assertEqual(r_data["description"], self.permission_model.description)
        self.assertEqual(r_data["id"], self.permission_model.id)

    def test_permission_delete(self):
        """Test case for permission_delete
        """
        data = {
            "name": ("%s" % uuid.uuid1())[:30],
            "description": "permission to delete",
        }
        model = db_actions.crud(
            model="Permission",
            api_model=Permission,
            data=data,
            action="create"
        )
        response = self.client.open(
            '/api/v1/permissions/{permission_id}'.format(permission_id=model.id),
            method='DELETE', headers=self.headers)

        with self.assertRaises(werkzeug.exceptions.NotFound):
            db_actions.crud(
                model="Permission",
                api_model=Permission,
                action="read",
                query={"id": model.id}
            )

    def test_permission_list(self):
        """Test case for permission_list
        """
        objects = []
        for index in range(1, random.randint(5, 20)):
            data = {
                "name": ("%s" % uuid.uuid1())[:30],
                "description": "permission list %s" % index,
            }
            objects.append(db_actions.crud(
                model="Permission",
                api_model=Permission,
                data=data,
                action="create"
            ))
        query_string = [#('offset', 0),
                        ('permission_ids', ",".join(map(str, [permission.id for permission in objects])))]
        response = self.client.open(
            '/api/v1/permissions',
            method='GET',
            query_string=query_string,
            headers=self.headers)
        r_data = json.loads(response.data)
        self.assertEqual(len(r_data), len(objects))
        self.assertEqual(int(response.headers["X-Total-Count"]), len(objects))
        query_string = [('limit', 2),
                        ('permission_ids', ",".join(map(str, [permission.id for permission in objects])))]
        response = self.client.open(
            '/api/v1/permissions',
            method='GET',
            query_string=query_string,
            headers=self.headers)
        r_data = json.loads(response.data)
        self.assertEqual(len(r_data), 2)
        self.assertEqual(int(response.headers["X-Total-Count"]), len(objects))

    def test_permission_update(self):
        """Test case for permission_update
        """
        data = {
            "name": ("%s" % uuid.uuid1())[:30],
            "description": "permission to update",
        }
        model = db_actions.crud(
            model="Permission",
            api_model=Permission,
            data=data,
            action="create"
        )
        data = {
            "name": ("%s" % uuid.uuid1())[:30],
            "description": "permission updated",
        }
        data = PermissionUpdate(
            **data
        )
        response = self.client.open(
            '/api/v1/permissions/{permission_id}'.format(permission_id=model.id),
            method='PUT',
            data=json.dumps(data),
            content_type='application/json',
            headers=self.headers)
        r_data = json.loads(response.data)
        updated_entry = db_actions.crud(
            model="Permission",
            api_model=Permission,
            action="read",
            query={"id": model.id}
        )
        self.assertEqual(r_data["name"], updated_entry.name)
        self.assertEqual(r_data["description"], updated_entry.description)
