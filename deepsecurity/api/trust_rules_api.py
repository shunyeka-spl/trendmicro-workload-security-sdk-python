# coding: utf-8

"""
    Trend Micro Workload Security API

    Copyright 2018 - 2022 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Workload Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Workload Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 50.0.810
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsecurity.api_client import ApiClient


class TrustRulesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_trust_rule(self, trustrule, api_version, **kwargs):  # noqa: E501
        """Create a Trust Rule  # noqa: E501

        Create a new trust rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_trust_rule(trustrule, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationControlTrustRule trustrule: Settings of the new trust rule. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ApplicationControlTrustRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_trust_rule_with_http_info(trustrule, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_trust_rule_with_http_info(trustrule, api_version, **kwargs)  # noqa: E501
            return data

    def create_trust_rule_with_http_info(self, trustrule, api_version, **kwargs):  # noqa: E501
        """Create a Trust Rule  # noqa: E501

        Create a new trust rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_trust_rule_with_http_info(trustrule, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApplicationControlTrustRule trustrule: Settings of the new trust rule. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ApplicationControlTrustRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trustrule', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_trust_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'trustrule' is set
        if ('trustrule' not in params or
                params['trustrule'] is None):
            raise ValueError("Missing the required parameter `trustrule` when calling `create_trust_rule`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_trust_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'trustrule' in params:
            body_params = params['trustrule']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Legacy API Key', 'Trend Micro Cloud One API Key']  # noqa: E501

        return self.api_client.call_api(
            '/applicationcontroltrustrules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationControlTrustRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_trust_rule(self, ac_trust_rule_id, api_version, **kwargs):  # noqa: E501
        """Delete a Trust Rule.  # noqa: E501

        Delete a trust rule by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_trust_rule(ac_trust_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ac_trust_rule_id: The ID number of the trust rule to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_trust_rule_with_http_info(ac_trust_rule_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_trust_rule_with_http_info(ac_trust_rule_id, api_version, **kwargs)  # noqa: E501
            return data

    def delete_trust_rule_with_http_info(self, ac_trust_rule_id, api_version, **kwargs):  # noqa: E501
        """Delete a Trust Rule.  # noqa: E501

        Delete a trust rule by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_trust_rule_with_http_info(ac_trust_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ac_trust_rule_id: The ID number of the trust rule to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ac_trust_rule_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_trust_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ac_trust_rule_id' is set
        if ('ac_trust_rule_id' not in params or
                params['ac_trust_rule_id'] is None):
            raise ValueError("Missing the required parameter `ac_trust_rule_id` when calling `delete_trust_rule`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `delete_trust_rule`")  # noqa: E501

        if 'ac_trust_rule_id' in params and not re.search('\\d+', str(params['ac_trust_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `ac_trust_rule_id` when calling `delete_trust_rule`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'ac_trust_rule_id' in params:
            path_params['acTrustRuleID'] = params['ac_trust_rule_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Legacy API Key', 'Trend Micro Cloud One API Key']  # noqa: E501

        return self.api_client.call_api(
            '/applicationcontroltrustrules/{acTrustRuleID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def describe_trust_rule(self, ac_trust_rule_id, api_version, **kwargs):  # noqa: E501
        """Describe a Trust Rule  # noqa: E501

        Describe a trust rule by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_trust_rule(ac_trust_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ac_trust_rule_id: The ID number of the trust rule to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ApplicationControlTrustRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_trust_rule_with_http_info(ac_trust_rule_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_trust_rule_with_http_info(ac_trust_rule_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_trust_rule_with_http_info(self, ac_trust_rule_id, api_version, **kwargs):  # noqa: E501
        """Describe a Trust Rule  # noqa: E501

        Describe a trust rule by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_trust_rule_with_http_info(ac_trust_rule_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ac_trust_rule_id: The ID number of the trust rule to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ApplicationControlTrustRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ac_trust_rule_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_trust_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ac_trust_rule_id' is set
        if ('ac_trust_rule_id' not in params or
                params['ac_trust_rule_id'] is None):
            raise ValueError("Missing the required parameter `ac_trust_rule_id` when calling `describe_trust_rule`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_trust_rule`")  # noqa: E501

        if 'ac_trust_rule_id' in params and not re.search('\\d+', str(params['ac_trust_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `ac_trust_rule_id` when calling `describe_trust_rule`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'ac_trust_rule_id' in params:
            path_params['acTrustRuleID'] = params['ac_trust_rule_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Legacy API Key', 'Trend Micro Cloud One API Key']  # noqa: E501

        return self.api_client.call_api(
            '/applicationcontroltrustrules/{acTrustRuleID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationControlTrustRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_trust_rules(self, api_version, **kwargs):  # noqa: E501
        """List all Trust Rules  # noqa: E501

        List all trust rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_trust_rules(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: TrustRules
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_trust_rules_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_trust_rules_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def list_trust_rules_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """List all Trust Rules  # noqa: E501

        List all trust rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_trust_rules_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: TrustRules
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_trust_rules" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_trust_rules`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Legacy API Key', 'Trend Micro Cloud One API Key']  # noqa: E501

        return self.api_client.call_api(
            '/applicationcontroltrustrules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TrustRules',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_trust_rule(self, ac_trust_rule_id, request_trust_ruleset_update, api_version, **kwargs):  # noqa: E501
        """Modify a Trust Rule  # noqa: E501

        Modify a trust rule by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_trust_rule(ac_trust_rule_id, request_trust_ruleset_update, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ac_trust_rule_id: The ID of the trust rule to modify. (required)
        :param TrustRuleUpdateRequest request_trust_ruleset_update: The attributes of the trust rule to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ApplicationControlTrustRule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_trust_rule_with_http_info(ac_trust_rule_id, request_trust_ruleset_update, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_trust_rule_with_http_info(ac_trust_rule_id, request_trust_ruleset_update, api_version, **kwargs)  # noqa: E501
            return data

    def modify_trust_rule_with_http_info(self, ac_trust_rule_id, request_trust_ruleset_update, api_version, **kwargs):  # noqa: E501
        """Modify a Trust Rule  # noqa: E501

        Modify a trust rule by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_trust_rule_with_http_info(ac_trust_rule_id, request_trust_ruleset_update, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int ac_trust_rule_id: The ID of the trust rule to modify. (required)
        :param TrustRuleUpdateRequest request_trust_ruleset_update: The attributes of the trust rule to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: ApplicationControlTrustRule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ac_trust_rule_id', 'request_trust_ruleset_update', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_trust_rule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ac_trust_rule_id' is set
        if ('ac_trust_rule_id' not in params or
                params['ac_trust_rule_id'] is None):
            raise ValueError("Missing the required parameter `ac_trust_rule_id` when calling `modify_trust_rule`")  # noqa: E501
        # verify the required parameter 'request_trust_ruleset_update' is set
        if ('request_trust_ruleset_update' not in params or
                params['request_trust_ruleset_update'] is None):
            raise ValueError("Missing the required parameter `request_trust_ruleset_update` when calling `modify_trust_rule`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_trust_rule`")  # noqa: E501

        if 'ac_trust_rule_id' in params and not re.search('\\d+', str(params['ac_trust_rule_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `ac_trust_rule_id` when calling `modify_trust_rule`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'ac_trust_rule_id' in params:
            path_params['acTrustRuleID'] = params['ac_trust_rule_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_trust_ruleset_update' in params:
            body_params = params['request_trust_ruleset_update']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Legacy API Key', 'Trend Micro Cloud One API Key']  # noqa: E501

        return self.api_client.call_api(
            '/applicationcontroltrustrules/{acTrustRuleID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationControlTrustRule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
