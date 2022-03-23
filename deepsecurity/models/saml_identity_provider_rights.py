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


class SamlIdentityProviderRights(object):
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
        'can_create_new_saml_identity_providers': 'bool',
        'can_delete_saml_identity_providers': 'bool',
        'can_edit_saml_identity_providers': 'bool',
        'can_view_saml_identity_providers': 'bool'
    }

    attribute_map = {
        'can_create_new_saml_identity_providers': 'canCreateNewSAMLIdentityProviders',
        'can_delete_saml_identity_providers': 'canDeleteSAMLIdentityProviders',
        'can_edit_saml_identity_providers': 'canEditSAMLIdentityProviders',
        'can_view_saml_identity_providers': 'canViewSAMLIdentityProviders'
    }

    def __init__(self, can_create_new_saml_identity_providers=None, can_delete_saml_identity_providers=None, can_edit_saml_identity_providers=None, can_view_saml_identity_providers=None):  # noqa: E501
        """SamlIdentityProviderRights - a model defined in Swagger"""  # noqa: E501

        self._can_create_new_saml_identity_providers = None
        self._can_delete_saml_identity_providers = None
        self._can_edit_saml_identity_providers = None
        self._can_view_saml_identity_providers = None
        self.discriminator = None

        if can_create_new_saml_identity_providers is not None:
            self.can_create_new_saml_identity_providers = can_create_new_saml_identity_providers
        if can_delete_saml_identity_providers is not None:
            self.can_delete_saml_identity_providers = can_delete_saml_identity_providers
        if can_edit_saml_identity_providers is not None:
            self.can_edit_saml_identity_providers = can_edit_saml_identity_providers
        if can_view_saml_identity_providers is not None:
            self.can_view_saml_identity_providers = can_view_saml_identity_providers

    @property
    def can_create_new_saml_identity_providers(self):
        """Gets the can_create_new_saml_identity_providers of this SamlIdentityProviderRights.  # noqa: E501

        Right to create new SAML identity providers.  # noqa: E501

        :return: The can_create_new_saml_identity_providers of this SamlIdentityProviderRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_create_new_saml_identity_providers

    @can_create_new_saml_identity_providers.setter
    def can_create_new_saml_identity_providers(self, can_create_new_saml_identity_providers):
        """Sets the can_create_new_saml_identity_providers of this SamlIdentityProviderRights.

        Right to create new SAML identity providers.  # noqa: E501

        :param can_create_new_saml_identity_providers: The can_create_new_saml_identity_providers of this SamlIdentityProviderRights.  # noqa: E501
        :type: bool
        """

        self._can_create_new_saml_identity_providers = can_create_new_saml_identity_providers

    @property
    def can_delete_saml_identity_providers(self):
        """Gets the can_delete_saml_identity_providers of this SamlIdentityProviderRights.  # noqa: E501

        Right to delete SAML identity providers.  # noqa: E501

        :return: The can_delete_saml_identity_providers of this SamlIdentityProviderRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete_saml_identity_providers

    @can_delete_saml_identity_providers.setter
    def can_delete_saml_identity_providers(self, can_delete_saml_identity_providers):
        """Sets the can_delete_saml_identity_providers of this SamlIdentityProviderRights.

        Right to delete SAML identity providers.  # noqa: E501

        :param can_delete_saml_identity_providers: The can_delete_saml_identity_providers of this SamlIdentityProviderRights.  # noqa: E501
        :type: bool
        """

        self._can_delete_saml_identity_providers = can_delete_saml_identity_providers

    @property
    def can_edit_saml_identity_providers(self):
        """Gets the can_edit_saml_identity_providers of this SamlIdentityProviderRights.  # noqa: E501

        Right to edit SAML identity providers.  # noqa: E501

        :return: The can_edit_saml_identity_providers of this SamlIdentityProviderRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit_saml_identity_providers

    @can_edit_saml_identity_providers.setter
    def can_edit_saml_identity_providers(self, can_edit_saml_identity_providers):
        """Sets the can_edit_saml_identity_providers of this SamlIdentityProviderRights.

        Right to edit SAML identity providers.  # noqa: E501

        :param can_edit_saml_identity_providers: The can_edit_saml_identity_providers of this SamlIdentityProviderRights.  # noqa: E501
        :type: bool
        """

        self._can_edit_saml_identity_providers = can_edit_saml_identity_providers

    @property
    def can_view_saml_identity_providers(self):
        """Gets the can_view_saml_identity_providers of this SamlIdentityProviderRights.  # noqa: E501

        Right to view SAML identity providers.  # noqa: E501

        :return: The can_view_saml_identity_providers of this SamlIdentityProviderRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_view_saml_identity_providers

    @can_view_saml_identity_providers.setter
    def can_view_saml_identity_providers(self, can_view_saml_identity_providers):
        """Sets the can_view_saml_identity_providers of this SamlIdentityProviderRights.

        Right to view SAML identity providers.  # noqa: E501

        :param can_view_saml_identity_providers: The can_view_saml_identity_providers of this SamlIdentityProviderRights.  # noqa: E501
        :type: bool
        """

        self._can_view_saml_identity_providers = can_view_saml_identity_providers

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
        if issubclass(SamlIdentityProviderRights, dict):
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
        if not isinstance(other, SamlIdentityProviderRights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

