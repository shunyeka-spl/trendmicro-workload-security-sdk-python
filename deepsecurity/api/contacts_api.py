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


class ContactsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_contact(self, contact, api_version, **kwargs):  # noqa: E501
        """Create a Contact  # noqa: E501

        Create a new contact.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_contact(contact, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Contact contact: The settings of the contact to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_contact_with_http_info(contact, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_contact_with_http_info(contact, api_version, **kwargs)  # noqa: E501
            return data

    def create_contact_with_http_info(self, contact, api_version, **kwargs):  # noqa: E501
        """Create a Contact  # noqa: E501

        Create a new contact.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_contact_with_http_info(contact, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Contact contact: The settings of the contact to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contact', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_contact" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contact' is set
        if ('contact' not in params or
                params['contact'] is None):
            raise ValueError("Missing the required parameter `contact` when calling `create_contact`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_contact`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contact' in params:
            body_params = params['contact']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Legacy API Key', 'Trend Micro Cloud One API Key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Contact',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_contact(self, contact_id, api_version, **kwargs):  # noqa: E501
        """Delete a Contact  # noqa: E501

        Delete a contact by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_contact(contact_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: The ID number of the contact to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_contact_with_http_info(contact_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_contact_with_http_info(contact_id, api_version, **kwargs)  # noqa: E501
            return data

    def delete_contact_with_http_info(self, contact_id, api_version, **kwargs):  # noqa: E501
        """Delete a Contact  # noqa: E501

        Delete a contact by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_contact_with_http_info(contact_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: The ID number of the contact to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contact_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_contact" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params or
                params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `delete_contact`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `delete_contact`")  # noqa: E501

        if 'contact_id' in params and not re.search('\\d+', str(params['contact_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `contact_id` when calling `delete_contact`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'contact_id' in params:
            path_params['contactID'] = params['contact_id']  # noqa: E501

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
            '/contacts/{contactID}', 'DELETE',
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

    def describe_contact(self, contact_id, api_version, **kwargs):  # noqa: E501
        """Describe a Contact  # noqa: E501

        Describe a contact by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_contact(contact_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: The ID number of the contact to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_contact_with_http_info(contact_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_contact_with_http_info(contact_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_contact_with_http_info(self, contact_id, api_version, **kwargs):  # noqa: E501
        """Describe a Contact  # noqa: E501

        Describe a contact by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_contact_with_http_info(contact_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: The ID number of the contact to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contact_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_contact" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params or
                params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `describe_contact`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_contact`")  # noqa: E501

        if 'contact_id' in params and not re.search('\\d+', str(params['contact_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `contact_id` when calling `describe_contact`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'contact_id' in params:
            path_params['contactID'] = params['contact_id']  # noqa: E501

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
            '/contacts/{contactID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Contact',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_contacts(self, api_version, **kwargs):  # noqa: E501
        """List Contacts  # noqa: E501

        Lists all contacts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_contacts(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: Contacts
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_contacts_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_contacts_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def list_contacts_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """List Contacts  # noqa: E501

        Lists all contacts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_contacts_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: Contacts
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
                    " to method list_contacts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_contacts`")  # noqa: E501

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
            '/contacts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Contacts',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_contact(self, contact_id, contact, api_version, **kwargs):  # noqa: E501
        """Modify a Contact  # noqa: E501

        Modify a contact by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_contact(contact_id, contact, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: The ID number of the contact to modify. (required)
        :param Contact contact: The settings of the contact to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_contact_with_http_info(contact_id, contact, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_contact_with_http_info(contact_id, contact, api_version, **kwargs)  # noqa: E501
            return data

    def modify_contact_with_http_info(self, contact_id, contact, api_version, **kwargs):  # noqa: E501
        """Modify a Contact  # noqa: E501

        Modify a contact by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_contact_with_http_info(contact_id, contact, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int contact_id: The ID number of the contact to modify. (required)
        :param Contact contact: The settings of the contact to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: Contact
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contact_id', 'contact', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_contact" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params or
                params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `modify_contact`")  # noqa: E501
        # verify the required parameter 'contact' is set
        if ('contact' not in params or
                params['contact'] is None):
            raise ValueError("Missing the required parameter `contact` when calling `modify_contact`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_contact`")  # noqa: E501

        if 'contact_id' in params and not re.search('\\d+', str(params['contact_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `contact_id` when calling `modify_contact`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'contact_id' in params:
            path_params['contactID'] = params['contact_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contact' in params:
            body_params = params['contact']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Legacy API Key', 'Trend Micro Cloud One API Key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/{contactID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Contact',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_contacts(self, api_version, **kwargs):  # noqa: E501
        """Search Contacts  # noqa: E501

        Search for contacts using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_contacts(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: Contacts
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_contacts_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.search_contacts_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def search_contacts_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Search Contacts  # noqa: E501

        Search for contacts using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_contacts_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: Contacts
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
                    " to method search_contacts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `search_contacts`")  # noqa: E501

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
        auth_settings = ['Legacy API Key', 'Trend Micro Cloud One API Key']  # noqa: E501

        return self.api_client.call_api(
            '/contacts/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Contacts',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
