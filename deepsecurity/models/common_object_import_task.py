# coding: utf-8

"""
    Trend Micro Workload Security API

    Copyright 2018 - 2022 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Workload Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Workload Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 50.0.810
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from deepsecurity.models.common_object_mapping import CommonObjectMapping  # noqa: F401,E501


class CommonObjectImportTask(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'common_object_content': 'str',
        'type': 'str',
        'status': 'str',
        'created': 'int',
        'last_updated': 'int',
        'common_object_mappings': 'list[CommonObjectMapping]',
        'error_code': 'int',
        'id': 'int',
        'task_guid': 'str'
    }

    attribute_map = {
        'common_object_content': 'commonObjectContent',
        'type': 'type',
        'status': 'status',
        'created': 'created',
        'last_updated': 'lastUpdated',
        'common_object_mappings': 'commonObjectMappings',
        'error_code': 'errorCode',
        'id': 'ID',
        'task_guid': 'taskGUID'
    }

    def __init__(self, common_object_content=None, type=None, status=None, created=None, last_updated=None, common_object_mappings=None, error_code=None, id=None, task_guid=None):  # noqa: E501
        """CommonObjectImportTask - a model defined in Swagger"""  # noqa: E501

        self._common_object_content = None
        self._type = None
        self._status = None
        self._created = None
        self._last_updated = None
        self._common_object_mappings = None
        self._error_code = None
        self._id = None
        self._task_guid = None
        self.discriminator = None

        self.common_object_content = common_object_content
        self.type = type
        if status is not None:
            self.status = status
        if created is not None:
            self.created = created
        if last_updated is not None:
            self.last_updated = last_updated
        if common_object_mappings is not None:
            self.common_object_mappings = common_object_mappings
        if error_code is not None:
            self.error_code = error_code
        if id is not None:
            self.id = id
        if task_guid is not None:
            self.task_guid = task_guid

    @property
    def common_object_content(self):
        """Gets the common_object_content of this CommonObjectImportTask.  # noqa: E501

        Common object content zipped and base64-encoded, write only.  # noqa: E501

        :return: The common_object_content of this CommonObjectImportTask.  # noqa: E501
        :rtype: str
        """
        return self._common_object_content

    @common_object_content.setter
    def common_object_content(self, common_object_content):
        """Sets the common_object_content of this CommonObjectImportTask.

        Common object content zipped and base64-encoded, write only.  # noqa: E501

        :param common_object_content: The common_object_content of this CommonObjectImportTask.  # noqa: E501
        :type: str
        """
        if common_object_content is None:
            raise ValueError("Invalid value for `common_object_content`, must not be `None`")  # noqa: E501

        self._common_object_content = common_object_content

    @property
    def type(self):
        """Gets the type of this CommonObjectImportTask.  # noqa: E501

        Type of the common objects to import. Searchable as Choice.  # noqa: E501

        :return: The type of this CommonObjectImportTask.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CommonObjectImportTask.

        Type of the common objects to import. Searchable as Choice.  # noqa: E501

        :param type: The type of this CommonObjectImportTask.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["directory-lists", "file-extension-lists", "file-lists", "ip-lists", "mac-lists", "port-lists", "contexts", "stateful-configurations", "schedules"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def status(self):
        """Gets the status of this CommonObjectImportTask.  # noqa: E501

        Status of the task.  # noqa: E501

        :return: The status of this CommonObjectImportTask.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CommonObjectImportTask.

        Status of the task.  # noqa: E501

        :param status: The status of this CommonObjectImportTask.  # noqa: E501
        :type: str
        """
        allowed_values = ["requested", "in-progress", "complete", "failed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created(self):
        """Gets the created of this CommonObjectImportTask.  # noqa: E501

        Timestamp of the created time, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :return: The created of this CommonObjectImportTask.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CommonObjectImportTask.

        Timestamp of the created time, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :param created: The created of this CommonObjectImportTask.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def last_updated(self):
        """Gets the last_updated of this CommonObjectImportTask.  # noqa: E501

        Timestamp of the last updated time, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :return: The last_updated of this CommonObjectImportTask.  # noqa: E501
        :rtype: int
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this CommonObjectImportTask.

        Timestamp of the last updated time, in milliseconds since epoch. Searchable as Date.  # noqa: E501

        :param last_updated: The last_updated of this CommonObjectImportTask.  # noqa: E501
        :type: int
        """

        self._last_updated = last_updated

    @property
    def common_object_mappings(self):
        """Gets the common_object_mappings of this CommonObjectImportTask.  # noqa: E501

        Common object mapping between Deep Security Manager and Workload Security.  # noqa: E501

        :return: The common_object_mappings of this CommonObjectImportTask.  # noqa: E501
        :rtype: list[CommonObjectMapping]
        """
        return self._common_object_mappings

    @common_object_mappings.setter
    def common_object_mappings(self, common_object_mappings):
        """Sets the common_object_mappings of this CommonObjectImportTask.

        Common object mapping between Deep Security Manager and Workload Security.  # noqa: E501

        :param common_object_mappings: The common_object_mappings of this CommonObjectImportTask.  # noqa: E501
        :type: list[CommonObjectMapping]
        """

        self._common_object_mappings = common_object_mappings

    @property
    def error_code(self):
        """Gets the error_code of this CommonObjectImportTask.  # noqa: E501

        Type of failed import.  # noqa: E501

        :return: The error_code of this CommonObjectImportTask.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CommonObjectImportTask.

        Type of failed import.  # noqa: E501

        :param error_code: The error_code of this CommonObjectImportTask.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def id(self):
        """Gets the id of this CommonObjectImportTask.  # noqa: E501

        ID of the CommonObjectImportTask.  # noqa: E501

        :return: The id of this CommonObjectImportTask.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommonObjectImportTask.

        ID of the CommonObjectImportTask.  # noqa: E501

        :param id: The id of this CommonObjectImportTask.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def task_guid(self):
        """Gets the task_guid of this CommonObjectImportTask.  # noqa: E501

        GUID of the task. Searchable as String.  # noqa: E501

        :return: The task_guid of this CommonObjectImportTask.  # noqa: E501
        :rtype: str
        """
        return self._task_guid

    @task_guid.setter
    def task_guid(self, task_guid):
        """Sets the task_guid of this CommonObjectImportTask.

        GUID of the task. Searchable as String.  # noqa: E501

        :param task_guid: The task_guid of this CommonObjectImportTask.  # noqa: E501
        :type: str
        """

        self._task_guid = task_guid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CommonObjectImportTask, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CommonObjectImportTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

