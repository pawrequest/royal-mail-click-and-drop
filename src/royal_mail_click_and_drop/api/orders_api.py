from typing import Any, Dict, List, Optional, Tuple, Union
from datetime import datetime

from pydantic import Field, StrictFloat, StrictInt, StrictStr, validate_call
from typing_extensions import Annotated

from royal_mail_click_and_drop.models.create_orders_response import CreateOrdersResponse
from royal_mail_click_and_drop.models.delete_orders_resource import DeleteOrdersResource
from royal_mail_click_and_drop.models.get_order_details_resource import GetOrderDetailsResource
from royal_mail_click_and_drop.models.get_order_info_resource import GetOrderInfoResource
from royal_mail_click_and_drop.models.get_orders_details_response import GetOrdersDetailsResponse
from royal_mail_click_and_drop.models.get_orders_response import GetOrdersResponse
from royal_mail_click_and_drop.models.update_order_status_response import UpdateOrderStatusResponse
from royal_mail_click_and_drop.models.update_orders_status_request import UpdateOrdersStatusRequest
from royal_mail_click_and_drop.api_client import ApiClient, RequestSerialized
from royal_mail_click_and_drop.api_response import ApiResponse
from royal_mail_click_and_drop.rest import RESTResponseType
from royal_mail_click_and_drop.models.create_orders_request import CreateOrdersRequest


class OrdersApi:
    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def create_orders_async(
        self,
        create_orders_request: CreateOrdersRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> CreateOrdersResponse:
        """Create orders


        :param create_orders_request: (required)
        :type create_orders_request: CreateOrdersRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._create_orders_async_serialize(
            create_orders_request=create_orders_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'CreateOrdersResponse',
            '400': 'ErrorResponse',
            '401': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def create_orders_async_with_http_info(
        self,
        create_orders_request: CreateOrdersRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[CreateOrdersResponse]:
        """Create orders


        :param create_orders_request: (required)
        :type create_orders_request: CreateOrdersRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._create_orders_async_serialize(
            create_orders_request=create_orders_request.model_dump(by_alias=True, mode='json'),
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'CreateOrdersResponse',
            '400': 'ErrorResponse',
            '401': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def create_orders_async_without_preload_content(
        self,
        create_orders_request: CreateOrdersRequest,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Create orders


        :param create_orders_request: (required)
        :type create_orders_request: CreateOrdersRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._create_orders_async_serialize(
            create_orders_request=create_orders_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'CreateOrdersResponse',
            '400': 'ErrorResponse',
            '401': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _create_orders_async_serialize(
        self,
        create_orders_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if create_orders_request is not None:
            _body_params = create_orders_request

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(['application/json'])
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = ['Bearer']

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/orders',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def delete_orders_async(
        self,
        order_identifiers: Annotated[
            StrictStr,
            Field(
                description='One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.'
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> DeleteOrdersResource:
        """Delete orders

        Please be aware labels generated on orders which are deleted are no longer valid and must be destroyed.  Cancelled label information is automatically shared with Royal Mail Revenue Protection, and should a cancelled label be identified on an item in the Royal Mail Network, you will be charged on your account and an additional handling fee applied.

        :param order_identifiers: One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. (required)
        :type order_identifiers: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._delete_orders_async_serialize(
            order_identifiers=order_identifiers,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'DeleteOrdersResource',
            '400': 'List[OrderErrorInfo]',
            '401': None,
            '403': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def delete_orders_async_with_http_info(
        self,
        order_identifiers: Annotated[
            StrictStr,
            Field(
                description='One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.'
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[DeleteOrdersResource]:
        """Delete orders

        Please be aware labels generated on orders which are deleted are no longer valid and must be destroyed.  Cancelled label information is automatically shared with Royal Mail Revenue Protection, and should a cancelled label be identified on an item in the Royal Mail Network, you will be charged on your account and an additional handling fee applied.

        :param order_identifiers: One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. (required)
        :type order_identifiers: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._delete_orders_async_serialize(
            order_identifiers=order_identifiers,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'DeleteOrdersResource',
            '400': 'List[OrderErrorInfo]',
            '401': None,
            '403': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def delete_orders_async_without_preload_content(
        self,
        order_identifiers: Annotated[
            StrictStr,
            Field(
                description='One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.'
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Delete orders

        Please be aware labels generated on orders which are deleted are no longer valid and must be destroyed.  Cancelled label information is automatically shared with Royal Mail Revenue Protection, and should a cancelled label be identified on an item in the Royal Mail Network, you will be charged on your account and an additional handling fee applied.

        :param order_identifiers: One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. (required)
        :type order_identifiers: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._delete_orders_async_serialize(
            order_identifiers=order_identifiers,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'DeleteOrdersResource',
            '400': 'List[OrderErrorInfo]',
            '401': None,
            '403': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _delete_orders_async_serialize(
        self,
        order_identifiers,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if order_identifiers is not None:
            _path_params['orderIdentifiers'] = order_identifiers

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # authentication setting
        _auth_settings: List[str] = ['Bearer']

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/orders/{orderIdentifiers}',
            path_params=_path_params,
            header_params=_header_params,
            body=_body_params,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def get_orders_async(
        self,
        page_size: Annotated[
            Optional[Annotated[int, Field(le=100, strict=True, ge=1)]],
            Field(description='The number of items to return'),
        ] = None,
        start_date_time: Annotated[
            Optional[datetime], Field(description='Date and time lower bound for items filtering')
        ] = None,
        end_date_time: Annotated[
            Optional[datetime], Field(description='Date and time upper bound for items filtering')
        ] = None,
        continuation_token: Annotated[
            Optional[StrictStr],
            Field(description='The token for retrieving the next page of items'),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> GetOrdersResponse:
        """Retrieve pageable list of orders


        :param page_size: The number of items to return
        :type page_size: int
        :param start_date_time: Date and time lower bound for items filtering
        :type start_date_time: datetime
        :param end_date_time: Date and time upper bound for items filtering
        :type end_date_time: datetime
        :param continuation_token: The token for retrieving the next page of items
        :type continuation_token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_orders_async_serialize(
            page_size=page_size,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            continuation_token=continuation_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'GetOrdersResponse',
            '400': 'ErrorResponse',
            '401': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def get_orders_async_with_http_info(
        self,
        page_size: Annotated[
            Optional[Annotated[int, Field(le=100, strict=True, ge=1)]],
            Field(description='The number of items to return'),
        ] = None,
        start_date_time: Annotated[
            Optional[datetime], Field(description='Date and time lower bound for items filtering')
        ] = None,
        end_date_time: Annotated[
            Optional[datetime], Field(description='Date and time upper bound for items filtering')
        ] = None,
        continuation_token: Annotated[
            Optional[StrictStr],
            Field(description='The token for retrieving the next page of items'),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[GetOrdersResponse]:
        """Retrieve pageable list of orders


        :param page_size: The number of items to return
        :type page_size: int
        :param start_date_time: Date and time lower bound for items filtering
        :type start_date_time: datetime
        :param end_date_time: Date and time upper bound for items filtering
        :type end_date_time: datetime
        :param continuation_token: The token for retrieving the next page of items
        :type continuation_token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_orders_async_serialize(
            page_size=page_size,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            continuation_token=continuation_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'GetOrdersResponse',
            '400': 'ErrorResponse',
            '401': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def get_orders_async_without_preload_content(
        self,
        page_size: Annotated[
            Optional[Annotated[int, Field(le=100, strict=True, ge=1)]],
            Field(description='The number of items to return'),
        ] = None,
        start_date_time: Annotated[
            Optional[datetime], Field(description='Date and time lower bound for items filtering')
        ] = None,
        end_date_time: Annotated[
            Optional[datetime], Field(description='Date and time upper bound for items filtering')
        ] = None,
        continuation_token: Annotated[
            Optional[StrictStr],
            Field(description='The token for retrieving the next page of items'),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve pageable list of orders


        :param page_size: The number of items to return
        :type page_size: int
        :param start_date_time: Date and time lower bound for items filtering
        :type start_date_time: datetime
        :param end_date_time: Date and time upper bound for items filtering
        :type end_date_time: datetime
        :param continuation_token: The token for retrieving the next page of items
        :type continuation_token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_orders_async_serialize(
            page_size=page_size,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            continuation_token=continuation_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'GetOrdersResponse',
            '400': 'ErrorResponse',
            '401': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _get_orders_async_serialize(
        self,
        page_size,
        start_date_time,
        end_date_time,
        continuation_token,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if page_size is not None:
            _query_params.append(('pageSize', page_size))

        if start_date_time is not None:
            if isinstance(start_date_time, datetime):
                _query_params.append(
                    (
                        'startDateTime',
                        start_date_time.strftime(self.api_client.configuration.datetime_format),
                    )
                )
            else:
                _query_params.append(('startDateTime', start_date_time))

        if end_date_time is not None:
            if isinstance(end_date_time, datetime):
                _query_params.append(
                    (
                        'endDateTime',
                        end_date_time.strftime(self.api_client.configuration.datetime_format),
                    )
                )
            else:
                _query_params.append(('endDateTime', end_date_time))

        if continuation_token is not None:
            _query_params.append(('continuationToken', continuation_token))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # authentication setting
        _auth_settings: List[str] = ['Bearer']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/orders',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def get_orders_with_details_async(
        self,
        page_size: Annotated[
            Optional[Annotated[int, Field(le=100, strict=True, ge=1)]],
            Field(description='The number of items to return'),
        ] = None,
        start_date_time: Annotated[
            Optional[datetime], Field(description='Date and time lower bound for items filtering')
        ] = None,
        end_date_time: Annotated[
            Optional[datetime], Field(description='Date and time upper bound for items filtering')
        ] = None,
        continuation_token: Annotated[
            Optional[StrictStr],
            Field(description='The token for retrieving the next page of items'),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> GetOrdersDetailsResponse:
        """Retrieve pageable list of orders with details

        <b>Reserved for ChannelShipper customers only - please visit <a href=\"https://channelshipper.com/\" target=\"_self\">ChannelShipper.com</a> for more information</b>

        :param page_size: The number of items to return
        :type page_size: int
        :param start_date_time: Date and time lower bound for items filtering
        :type start_date_time: datetime
        :param end_date_time: Date and time upper bound for items filtering
        :type end_date_time: datetime
        :param continuation_token: The token for retrieving the next page of items
        :type continuation_token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_orders_with_details_async_serialize(
            page_size=page_size,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            continuation_token=continuation_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'GetOrdersDetailsResponse',
            '400': 'ErrorResponse',
            '401': None,
            '403': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def get_orders_with_details_async_with_http_info(
        self,
        page_size: Annotated[
            Optional[Annotated[int, Field(le=100, strict=True, ge=1)]],
            Field(description='The number of items to return'),
        ] = None,
        start_date_time: Annotated[
            Optional[datetime], Field(description='Date and time lower bound for items filtering')
        ] = None,
        end_date_time: Annotated[
            Optional[datetime], Field(description='Date and time upper bound for items filtering')
        ] = None,
        continuation_token: Annotated[
            Optional[StrictStr],
            Field(description='The token for retrieving the next page of items'),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[GetOrdersDetailsResponse]:
        """Retrieve pageable list of orders with details

        <b>Reserved for ChannelShipper customers only - please visit <a href=\"https://channelshipper.com/\" target=\"_self\">ChannelShipper.com</a> for more information</b>

        :param page_size: The number of items to return
        :type page_size: int
        :param start_date_time: Date and time lower bound for items filtering
        :type start_date_time: datetime
        :param end_date_time: Date and time upper bound for items filtering
        :type end_date_time: datetime
        :param continuation_token: The token for retrieving the next page of items
        :type continuation_token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_orders_with_details_async_serialize(
            page_size=page_size,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            continuation_token=continuation_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'GetOrdersDetailsResponse',
            '400': 'ErrorResponse',
            '401': None,
            '403': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def get_orders_with_details_async_without_preload_content(
        self,
        page_size: Annotated[
            Optional[Annotated[int, Field(le=100, strict=True, ge=1)]],
            Field(description='The number of items to return'),
        ] = None,
        start_date_time: Annotated[
            Optional[datetime], Field(description='Date and time lower bound for items filtering')
        ] = None,
        end_date_time: Annotated[
            Optional[datetime], Field(description='Date and time upper bound for items filtering')
        ] = None,
        continuation_token: Annotated[
            Optional[StrictStr],
            Field(description='The token for retrieving the next page of items'),
        ] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve pageable list of orders with details

        <b>Reserved for ChannelShipper customers only - please visit <a href=\"https://channelshipper.com/\" target=\"_self\">ChannelShipper.com</a> for more information</b>

        :param page_size: The number of items to return
        :type page_size: int
        :param start_date_time: Date and time lower bound for items filtering
        :type start_date_time: datetime
        :param end_date_time: Date and time upper bound for items filtering
        :type end_date_time: datetime
        :param continuation_token: The token for retrieving the next page of items
        :type continuation_token: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_orders_with_details_async_serialize(
            page_size=page_size,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            continuation_token=continuation_token,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'GetOrdersDetailsResponse',
            '400': 'ErrorResponse',
            '401': None,
            '403': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _get_orders_with_details_async_serialize(
        self,
        page_size,
        start_date_time,
        end_date_time,
        continuation_token,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if page_size is not None:
            _query_params.append(('pageSize', page_size))

        if start_date_time is not None:
            if isinstance(start_date_time, datetime):
                _query_params.append(
                    (
                        'startDateTime',
                        start_date_time.strftime(self.api_client.configuration.datetime_format),
                    )
                )
            else:
                _query_params.append(('startDateTime', start_date_time))

        if end_date_time is not None:
            if isinstance(end_date_time, datetime):
                _query_params.append(
                    (
                        'endDateTime',
                        end_date_time.strftime(self.api_client.configuration.datetime_format),
                    )
                )
            else:
                _query_params.append(('endDateTime', end_date_time))

        if continuation_token is not None:
            _query_params.append(('continuationToken', continuation_token))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # authentication setting
        _auth_settings: List[str] = ['Bearer']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/orders/full',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def get_specific_orders_async(
        self,
        order_identifiers: Annotated[
            StrictStr,
            Field(
                description='One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.'
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[GetOrderInfoResource]:
        """Retrieve specific orders


        :param order_identifiers: One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. (required)
        :type order_identifiers: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_specific_orders_async_serialize(
            order_identifiers=order_identifiers,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'List[GetOrderInfoResource]',
            '400': 'List[OrderErrorResponse]',
            '401': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def get_specific_orders_async_with_http_info(
        self,
        order_identifiers: Annotated[
            StrictStr,
            Field(
                description='One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.'
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[GetOrderInfoResource]]:
        """Retrieve specific orders


        :param order_identifiers: One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. (required)
        :type order_identifiers: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_specific_orders_async_serialize(
            order_identifiers=order_identifiers,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'List[GetOrderInfoResource]',
            '400': 'List[OrderErrorResponse]',
            '401': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def get_specific_orders_async_without_preload_content(
        self,
        order_identifiers: Annotated[
            StrictStr,
            Field(
                description='One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.'
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve specific orders


        :param order_identifiers: One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. (required)
        :type order_identifiers: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_specific_orders_async_serialize(
            order_identifiers=order_identifiers,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'List[GetOrderInfoResource]',
            '400': 'List[OrderErrorResponse]',
            '401': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _get_specific_orders_async_serialize(
        self,
        order_identifiers,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if order_identifiers is not None:
            _path_params['orderIdentifiers'] = order_identifiers
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # authentication setting
        _auth_settings: List[str] = ['Bearer']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/orders/{orderIdentifiers}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def get_specific_orders_with_details_async(
        self,
        order_identifiers: Annotated[
            StrictStr,
            Field(
                description='One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.'
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[GetOrderDetailsResource]:
        """Retrieve details of the specific orders

        <b>Reserved for ChannelShipper customers only - please visit <a href=\"https://channelshipper.com/\" target=\"_self\">ChannelShipper.com</a> for more information</b>

        :param order_identifiers: One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. (required)
        :type order_identifiers: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_specific_orders_with_details_async_serialize(
            order_identifiers=order_identifiers,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'List[GetOrderDetailsResource]',
            '400': 'List[OrderErrorResponse]',
            '401': None,
            '403': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def get_specific_orders_with_details_async_with_http_info(
        self,
        order_identifiers: Annotated[
            StrictStr,
            Field(
                description='One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.'
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[GetOrderDetailsResource]]:
        """Retrieve details of the specific orders

        <b>Reserved for ChannelShipper customers only - please visit <a href=\"https://channelshipper.com/\" target=\"_self\">ChannelShipper.com</a> for more information</b>

        :param order_identifiers: One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. (required)
        :type order_identifiers: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_specific_orders_with_details_async_serialize(
            order_identifiers=order_identifiers,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'List[GetOrderDetailsResource]',
            '400': 'List[OrderErrorResponse]',
            '401': None,
            '403': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def get_specific_orders_with_details_async_without_preload_content(
        self,
        order_identifiers: Annotated[
            StrictStr,
            Field(
                description='One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.'
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve details of the specific orders

        <b>Reserved for ChannelShipper customers only - please visit <a href=\"https://channelshipper.com/\" target=\"_self\">ChannelShipper.com</a> for more information</b>

        :param order_identifiers: One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. (required)
        :type order_identifiers: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._get_specific_orders_with_details_async_serialize(
            order_identifiers=order_identifiers,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'List[GetOrderDetailsResource]',
            '400': 'List[OrderErrorResponse]',
            '401': None,
            '403': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _get_specific_orders_with_details_async_serialize(
        self,
        order_identifiers,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if order_identifiers is not None:
            _path_params['orderIdentifiers'] = order_identifiers
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(['application/json'])

        # authentication setting
        _auth_settings: List[str] = ['Bearer']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/orders/{orderIdentifiers}/full',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def update_orders_status_async(
        self,
        update_orders_status_request: Annotated[
            UpdateOrdersStatusRequest,
            Field(
                description="At least one of 'orderIdentifier' and 'orderReference' is required. Providing both is disallowed to avoid ambiguity.  When the status is set to 'despatchedByOtherCourier', if the optional parameter 'trackingNumber' is provided then the parameters 'despatchDate', 'shippingCarrier' and 'shippingService' are also required. The maximum collection length is 100. "
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> UpdateOrderStatusResponse:
        """Set order status


        :param update_orders_status_request: At least one of 'orderIdentifier' and 'orderReference' is required. Providing both is disallowed to avoid ambiguity.  When the status is set to 'despatchedByOtherCourier', if the optional parameter 'trackingNumber' is provided then the parameters 'despatchDate', 'shippingCarrier' and 'shippingService' are also required. The maximum collection length is 100.  (required)
        :type update_orders_status_request: UpdateOrdersStatusRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._update_orders_status_async_serialize(
            update_orders_status_request=update_orders_status_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'UpdateOrderStatusResponse',
            '400': 'List[OrderUpdateError]',
            '401': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def update_orders_status_async_with_http_info(
        self,
        update_orders_status_request: Annotated[
            UpdateOrdersStatusRequest,
            Field(
                description="At least one of 'orderIdentifier' and 'orderReference' is required. Providing both is disallowed to avoid ambiguity.  When the status is set to 'despatchedByOtherCourier', if the optional parameter 'trackingNumber' is provided then the parameters 'despatchDate', 'shippingCarrier' and 'shippingService' are also required. The maximum collection length is 100. "
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[UpdateOrderStatusResponse]:
        """Set order status


        :param update_orders_status_request: At least one of 'orderIdentifier' and 'orderReference' is required. Providing both is disallowed to avoid ambiguity.  When the status is set to 'despatchedByOtherCourier', if the optional parameter 'trackingNumber' is provided then the parameters 'despatchDate', 'shippingCarrier' and 'shippingService' are also required. The maximum collection length is 100.  (required)
        :type update_orders_status_request: UpdateOrdersStatusRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._update_orders_status_async_serialize(
            update_orders_status_request=update_orders_status_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'UpdateOrderStatusResponse',
            '400': 'List[OrderUpdateError]',
            '401': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def update_orders_status_async_without_preload_content(
        self,
        update_orders_status_request: Annotated[
            UpdateOrdersStatusRequest,
            Field(
                description="At least one of 'orderIdentifier' and 'orderReference' is required. Providing both is disallowed to avoid ambiguity.  When the status is set to 'despatchedByOtherCourier', if the optional parameter 'trackingNumber' is provided then the parameters 'despatchDate', 'shippingCarrier' and 'shippingService' are also required. The maximum collection length is 100. "
            ),
        ],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]],
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Set order status


        :param update_orders_status_request: At least one of 'orderIdentifier' and 'orderReference' is required. Providing both is disallowed to avoid ambiguity.  When the status is set to 'despatchedByOtherCourier', if the optional parameter 'trackingNumber' is provided then the parameters 'despatchDate', 'shippingCarrier' and 'shippingService' are also required. The maximum collection length is 100.  (required)
        :type update_orders_status_request: UpdateOrdersStatusRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """  # noqa: E501

        _param = self._update_orders_status_async_serialize(
            update_orders_status_request=update_orders_status_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': 'UpdateOrderStatusResponse',
            '400': 'List[OrderUpdateError]',
            '401': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _update_orders_status_async_serialize(
        self,
        update_orders_status_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: Dict[str, str] = {}

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if update_orders_status_request is not None:
            _body_params = update_orders_status_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'Bearer'
        ]

        return self.api_client.param_serialize(
            method='PUT',
            resource_path='/orders/status',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


