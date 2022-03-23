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

from deepsecurity.models.event_based_task import EventBasedTask  # noqa: F401,E501


class EventBasedTasks(object):
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
        'event_based_tasks': 'list[EventBasedTask]'
    }

    attribute_map = {
        'event_based_tasks': 'eventBasedTasks'
    }

    def __init__(self, event_based_tasks=None):  # noqa: E501
        """EventBasedTasks - a model defined in Swagger"""  # noqa: E501

        self._event_based_tasks = None
        self.discriminator = None

        if event_based_tasks is not None:
            self.event_based_tasks = event_based_tasks

    @property
    def event_based_tasks(self):
        """Gets the event_based_tasks of this EventBasedTasks.  # noqa: E501


        :return: The event_based_tasks of this EventBasedTasks.  # noqa: E501
        :rtype: list[EventBasedTask]
        """
        return self._event_based_tasks

    @event_based_tasks.setter
    def event_based_tasks(self, event_based_tasks):
        """Sets the event_based_tasks of this EventBasedTasks.


        :param event_based_tasks: The event_based_tasks of this EventBasedTasks.  # noqa: E501
        :type: list[EventBasedTask]
        """

        self._event_based_tasks = event_based_tasks

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
        if issubclass(EventBasedTasks, dict):
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
        if not isinstance(other, EventBasedTasks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

