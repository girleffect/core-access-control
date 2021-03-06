# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class HealthInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, host: str=None, server_timestamp: datetime=None, version: str=None, db_timestamp: datetime=None):  # noqa: E501
        """HealthInfo - a model defined in Swagger

        :param host: The host of this HealthInfo.  # noqa: E501
        :type host: str
        :param server_timestamp: The server_timestamp of this HealthInfo.  # noqa: E501
        :type server_timestamp: datetime
        :param version: The version of this HealthInfo.  # noqa: E501
        :type version: str
        :param db_timestamp: The db_timestamp of this HealthInfo.  # noqa: E501
        :type db_timestamp: datetime
        """
        self.swagger_types = {
            'host': str,
            'server_timestamp': datetime,
            'version': str,
            'db_timestamp': datetime
        }

        self.attribute_map = {
            'host': 'host',
            'server_timestamp': 'server_timestamp',
            'version': 'version',
            'db_timestamp': 'db_timestamp'
        }

        self._host = host
        self._server_timestamp = server_timestamp
        self._version = version
        self._db_timestamp = db_timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'HealthInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The health_info of this HealthInfo.  # noqa: E501
        :rtype: HealthInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def host(self) -> str:
        """Gets the host of this HealthInfo.


        :return: The host of this HealthInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host: str):
        """Sets the host of this HealthInfo.


        :param host: The host of this HealthInfo.
        :type host: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def server_timestamp(self) -> datetime:
        """Gets the server_timestamp of this HealthInfo.


        :return: The server_timestamp of this HealthInfo.
        :rtype: datetime
        """
        return self._server_timestamp

    @server_timestamp.setter
    def server_timestamp(self, server_timestamp: datetime):
        """Sets the server_timestamp of this HealthInfo.


        :param server_timestamp: The server_timestamp of this HealthInfo.
        :type server_timestamp: datetime
        """
        if server_timestamp is None:
            raise ValueError("Invalid value for `server_timestamp`, must not be `None`")  # noqa: E501

        self._server_timestamp = server_timestamp

    @property
    def version(self) -> str:
        """Gets the version of this HealthInfo.


        :return: The version of this HealthInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this HealthInfo.


        :param version: The version of this HealthInfo.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def db_timestamp(self) -> datetime:
        """Gets the db_timestamp of this HealthInfo.


        :return: The db_timestamp of this HealthInfo.
        :rtype: datetime
        """
        return self._db_timestamp

    @db_timestamp.setter
    def db_timestamp(self, db_timestamp: datetime):
        """Sets the db_timestamp of this HealthInfo.


        :param db_timestamp: The db_timestamp of this HealthInfo.
        :type db_timestamp: datetime
        """
        if db_timestamp is None:
            raise ValueError("Invalid value for `db_timestamp`, must not be `None`")  # noqa: E501

        self._db_timestamp = db_timestamp
