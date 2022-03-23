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


class CommonObjectImportTasksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_common_object_import_task(self, api_version, **kwargs):  # noqa: E501
        """Create a CommonObjectImportTask  # noqa: E501

        Create a task to import common objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_common_object_import_task(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param CommonObjectImportTask common_object_import_task: Common object import task to create.
        :return: CommonObjectImportTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_common_object_import_task_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_common_object_import_task_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def create_common_object_import_task_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Create a CommonObjectImportTask  # noqa: E501

        Create a task to import common objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_common_object_import_task_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param CommonObjectImportTask common_object_import_task: Common object import task to create.
        :return: CommonObjectImportTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'common_object_import_task']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_common_object_import_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_common_object_import_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'common_object_import_task' in params:
            body_params = params['common_object_import_task']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/commonobjectimporttasks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonObjectImportTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def describe_common_object_import_task(self, common_object_import_task_id, api_version, **kwargs):  # noqa: E501
        """Describe a CommonObjectImportTask  # noqa: E501

        Describe a common object import task by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_common_object_import_task(common_object_import_task_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int common_object_import_task_id: The ID number of the common object import task to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: CommonObjectImportTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_common_object_import_task_with_http_info(common_object_import_task_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_common_object_import_task_with_http_info(common_object_import_task_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_common_object_import_task_with_http_info(self, common_object_import_task_id, api_version, **kwargs):  # noqa: E501
        """Describe a CommonObjectImportTask  # noqa: E501

        Describe a common object import task by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_common_object_import_task_with_http_info(common_object_import_task_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int common_object_import_task_id: The ID number of the common object import task to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: CommonObjectImportTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['common_object_import_task_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_common_object_import_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'common_object_import_task_id' is set
        if ('common_object_import_task_id' not in params or
                params['common_object_import_task_id'] is None):
            raise ValueError("Missing the required parameter `common_object_import_task_id` when calling `describe_common_object_import_task`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_common_object_import_task`")  # noqa: E501

        if 'common_object_import_task_id' in params and not re.search('\\d+', str(params['common_object_import_task_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `common_object_import_task_id` when calling `describe_common_object_import_task`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'common_object_import_task_id' in params:
            path_params['commonObjectImportTaskID'] = params['common_object_import_task_id']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/commonobjectimporttasks/{commonObjectImportTaskID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonObjectImportTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_common_object_import_tasks(self, api_version, **kwargs):  # noqa: E501
        """List CommonObjectImportTasks  # noqa: E501

        List all common object import tasks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_common_object_import_tasks(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: CommonObjectImportTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_common_object_import_tasks_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_common_object_import_tasks_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def list_common_object_import_tasks_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """List CommonObjectImportTasks  # noqa: E501

        List all common object import tasks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_common_object_import_tasks_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: CommonObjectImportTasks
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
                    " to method list_common_object_import_tasks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_common_object_import_tasks`")  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/commonobjectimporttasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonObjectImportTasks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_common_object_import_tasks(self, api_version, **kwargs):  # noqa: E501
        """Search CommonObjectImportTasks  # noqa: E501

        Search for CommonObjectImportTasks using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_common_object_import_tasks(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: CommonObjectImportTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_common_object_import_tasks_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.search_common_object_import_tasks_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def search_common_object_import_tasks_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Search CommonObjectImportTasks  # noqa: E501

        Search for CommonObjectImportTasks using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_common_object_import_tasks_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: CommonObjectImportTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'search_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_common_object_import_tasks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `search_common_object_import_tasks`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'search_filter' in params:
            body_params = params['search_filter']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/commonobjectimporttasks/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonObjectImportTasks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
