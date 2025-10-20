from typing import Any

from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr, validate_call
from typing import Annotated

from royal_mail_click_and_drop.api_client import ApiClient, RequestSerialized
from royal_mail_click_and_drop.api_response import ApiResponse
from royal_mail_click_and_drop.rest import RESTResponseType


class LabelsApi:
    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def get_orders_label_async(
        self,
        order_identifiers: Annotated[
            StrictStr,
            Field(
                description='One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.'
            ),
        ],
        document_type: Annotated[
            StrictStr,
            Field(
                description='Document generation mode. When documentType is set to "postageLabel" the additional parameters below must be used. These additional parameters will be ignored when documentType is not set to "postageLabel"'
            ),
        ],
        include_returns_label: Annotated[
            StrictBool | None,
            Field(
                description="Include returns label. Required when documentType is set to 'postageLabel'"
            ),
        ] = None,
        include_cn: Annotated[
            StrictBool | None,
            Field(
                description='Include CN22/CN23 with label. Optional parameter. If this parameter is used the setting will override the default account behaviour specified in the "Label format" setting "Generate customs declarations with orders"'
            ),
        ] = None,
        _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> bytearray:
        """Return a single PDF file with generated label and/or associated document(s)

        <b>Reserved for OBA customers only</b>  The account \"Label format\" settings page will control the page format settings used to print the postage label and associated documents. Certain combinations of these settings may prevent associated documents from being printed together with the postage label within a single document. If this occurs the documentType option can be used in a separate call to print missing documents.

        :param order_identifiers: One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. (required)
        :type order_identifiers: str
        :param document_type: Document generation mode. When documentType is set to \"postageLabel\" the additional parameters below must be used. These additional parameters will be ignored when documentType is not set to \"postageLabel\" (required)
        :type document_type: str
        :param include_returns_label: Include returns label. Required when documentType is set to 'postageLabel'
        :type include_returns_label: bool
        :param include_cn: Include CN22/CN23 with label. Optional parameter. If this parameter is used the setting will override the default account behaviour specified in the \"Label format\" setting \"Generate customs declarations with orders\"
        :type include_cn: bool
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
        """
        _param = self._get_orders_label_async_serialize(
            order_identifiers=order_identifiers,
            document_type=document_type,
            include_returns_label=include_returns_label,
            include_cn=include_cn,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            '200': 'bytearray',
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
    def get_orders_label_async_with_http_info(
        self,
        order_identifiers: Annotated[
            StrictStr,
            Field(
                description='One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.'
            ),
        ],
        document_type: Annotated[
            StrictStr,
            Field(
                description='Document generation mode. When documentType is set to "postageLabel" the additional parameters below must be used. These additional parameters will be ignored when documentType is not set to "postageLabel"'
            ),
        ],
        include_returns_label: Annotated[
            StrictBool | None,
            Field(
                description="Include returns label. Required when documentType is set to 'postageLabel'"
            ),
        ] = None,
        include_cn: Annotated[
            StrictBool | None,
            Field(
                description='Include CN22/CN23 with label. Optional parameter. If this parameter is used the setting will override the default account behaviour specified in the "Label format" setting "Generate customs declarations with orders"'
            ),
        ] = None,
        _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[bytearray]:
        """Return a single PDF file with generated label and/or associated document(s)

        <b>Reserved for OBA customers only</b>  The account \"Label format\" settings page will control the page format settings used to print the postage label and associated documents. Certain combinations of these settings may prevent associated documents from being printed together with the postage label within a single document. If this occurs the documentType option can be used in a separate call to print missing documents.

        :param order_identifiers: One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. (required)
        :type order_identifiers: str
        :param document_type: Document generation mode. When documentType is set to \"postageLabel\" the additional parameters below must be used. These additional parameters will be ignored when documentType is not set to \"postageLabel\" (required)
        :type document_type: str
        :param include_returns_label: Include returns label. Required when documentType is set to 'postageLabel'
        :type include_returns_label: bool
        :param include_cn: Include CN22/CN23 with label. Optional parameter. If this parameter is used the setting will override the default account behaviour specified in the \"Label format\" setting \"Generate customs declarations with orders\"
        :type include_cn: bool
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
        """

        _param = self._get_orders_label_async_serialize(
            order_identifiers=order_identifiers,
            document_type=document_type,
            include_returns_label=include_returns_label,
            include_cn=include_cn,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            '200': 'bytearray',
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
    def get_orders_label_async_without_preload_content(
        self,
        order_identifiers: Annotated[
            StrictStr,
            Field(
                description='One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.'
            ),
        ],
        document_type: Annotated[
            StrictStr,
            Field(
                description='Document generation mode. When documentType is set to "postageLabel" the additional parameters below must be used. These additional parameters will be ignored when documentType is not set to "postageLabel"'
            ),
        ],
        include_returns_label: Annotated[
            StrictBool | None,
            Field(
                description="Include returns label. Required when documentType is set to 'postageLabel'"
            ),
        ] = None,
        include_cn: Annotated[
            StrictBool | None,
            Field(
                description='Include CN22/CN23 with label. Optional parameter. If this parameter is used the setting will override the default account behaviour specified in the "Label format" setting "Generate customs declarations with orders"'
            ),
        ] = None,
        _request_timeout: None | Annotated[StrictFloat, Field(gt=0)] | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Return a single PDF file with generated label and/or associated document(s)

        <b>Reserved for OBA customers only</b>  The account \"Label format\" settings page will control the page format settings used to print the postage label and associated documents. Certain combinations of these settings may prevent associated documents from being printed together with the postage label within a single document. If this occurs the documentType option can be used in a separate call to print missing documents.

        :param order_identifiers: One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. (required)
        :type order_identifiers: str
        :param document_type: Document generation mode. When documentType is set to \"postageLabel\" the additional parameters below must be used. These additional parameters will be ignored when documentType is not set to \"postageLabel\" (required)
        :type document_type: str
        :param include_returns_label: Include returns label. Required when documentType is set to 'postageLabel'
        :type include_returns_label: bool
        :param include_cn: Include CN22/CN23 with label. Optional parameter. If this parameter is used the setting will override the default account behaviour specified in the \"Label format\" setting \"Generate customs declarations with orders\"
        :type include_cn: bool
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
        """

        _param = self._get_orders_label_async_serialize(
            order_identifiers=order_identifiers,
            document_type=document_type,
            include_returns_label=include_returns_label,
            include_cn=include_cn,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            '200': 'bytearray',
            '400': 'List[OrderErrorResponse]',
            '401': None,
            '403': None,
            '404': None,
            '500': 'ErrorResponse',
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _get_orders_label_async_serialize(
        self,
        order_identifiers,
        document_type,
        include_returns_label,
        include_cn,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: dict[str, str] = {}

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[str, str | bytes | list[str] | list[bytes] | list[tuple[str, bytes]]] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if order_identifiers is not None:
            _path_params['orderIdentifiers'] = order_identifiers
        # process the query parameters
        if document_type is not None:
            _query_params.append(('documentType', document_type))

        if include_returns_label is not None:
            _query_params.append(('includeReturnsLabel', include_returns_label))

        if include_cn is not None:
            _query_params.append(('includeCN', include_cn))

        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                ['application/pdf', 'application/json']
            )

        # authentication setting
        _auth_settings: list[str] = ['Bearer']

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/orders/{orderIdentifiers}/label',
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


