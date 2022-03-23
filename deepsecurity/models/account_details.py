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


class AccountDetails(object):
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
        'license_mode': 'str',
        'cloud_one_account_id': 'str',
        'cloud_one_account_name': 'str'
    }

    attribute_map = {
        'license_mode': 'licenseMode',
        'cloud_one_account_id': 'cloudOneAccountID',
        'cloud_one_account_name': 'cloudOneAccountName'
    }

    def __init__(self, license_mode=None, cloud_one_account_id=None, cloud_one_account_name=None):  # noqa: E501
        """AccountDetails - a model defined in Swagger"""  # noqa: E501

        self._license_mode = None
        self._cloud_one_account_id = None
        self._cloud_one_account_name = None
        self.discriminator = None

        if license_mode is not None:
            self.license_mode = license_mode
        if cloud_one_account_id is not None:
            self.cloud_one_account_id = cloud_one_account_id
        if cloud_one_account_name is not None:
            self.cloud_one_account_name = cloud_one_account_name

    @property
    def license_mode(self):
        """Gets the license_mode of this AccountDetails.  # noqa: E501

        License mode of the current Cloud One Account.  # noqa: E501

        :return: The license_mode of this AccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._license_mode

    @license_mode.setter
    def license_mode(self, license_mode):
        """Sets the license_mode of this AccountDetails.

        License mode of the current Cloud One Account.  # noqa: E501

        :param license_mode: The license_mode of this AccountDetails.  # noqa: E501
        :type: str
        """

        self._license_mode = license_mode

    @property
    def cloud_one_account_id(self):
        """Gets the cloud_one_account_id of this AccountDetails.  # noqa: E501

        Account ID of the current Cloud One Account.  # noqa: E501

        :return: The cloud_one_account_id of this AccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._cloud_one_account_id

    @cloud_one_account_id.setter
    def cloud_one_account_id(self, cloud_one_account_id):
        """Sets the cloud_one_account_id of this AccountDetails.

        Account ID of the current Cloud One Account.  # noqa: E501

        :param cloud_one_account_id: The cloud_one_account_id of this AccountDetails.  # noqa: E501
        :type: str
        """

        self._cloud_one_account_id = cloud_one_account_id

    @property
    def cloud_one_account_name(self):
        """Gets the cloud_one_account_name of this AccountDetails.  # noqa: E501

        Account Name of the current Cloud One Account.  # noqa: E501

        :return: The cloud_one_account_name of this AccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._cloud_one_account_name

    @cloud_one_account_name.setter
    def cloud_one_account_name(self, cloud_one_account_name):
        """Sets the cloud_one_account_name of this AccountDetails.

        Account Name of the current Cloud One Account.  # noqa: E501

        :param cloud_one_account_name: The cloud_one_account_name of this AccountDetails.  # noqa: E501
        :type: str
        """

        self._cloud_one_account_name = cloud_one_account_name

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
        if issubclass(AccountDetails, dict):
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
        if not isinstance(other, AccountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

