# openapi_client.OrdersApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_orders_async**](OrdersApi.md#create_orders_async) | **POST** /orders | Create orders
[**delete_orders_async**](OrdersApi.md#delete_orders_async) | **DELETE** /orders/{orderIdentifiers} | Delete orders
[**get_orders_async**](OrdersApi.md#get_orders_async) | **GET** /orders | Retrieve pageable list of orders
[**get_orders_with_details_async**](OrdersApi.md#get_orders_with_details_async) | **GET** /orders/full | Retrieve pageable list of orders with details
[**get_specific_orders_async**](OrdersApi.md#get_specific_orders_async) | **GET** /orders/{orderIdentifiers} | Retrieve specific orders
[**get_specific_orders_with_details_async**](OrdersApi.md#get_specific_orders_with_details_async) | **GET** /orders/{orderIdentifiers}/full | Retrieve details of the specific orders
[**update_orders_status_async**](OrdersApi.md#update_orders_status_async) | **PUT** /orders/status | Set order status


# **create_orders_async**
> CreateOrdersResponse create_orders_async(create_orders_request)

Create orders

### Example

* Api Key Authentication (Bearer):

```python
import royal_mail_click_and_drop
from royal_mail_click_and_drop import CreateOrdersRequest
from royal_mail_click_and_drop import CreateOrdersResponse
from royal_mail_click_and_drop import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = royal_mail_click_and_drop.Configuration(
    host="/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with royal_mail_click_and_drop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = royal_mail_click_and_drop.OrdersApi(api_client)
    create_orders_request = royal_mail_click_and_drop.CreateOrdersRequest()  # CreateOrdersRequest | 

    try:
        # Create orders
        api_response = api_instance.create_orders_async(create_orders_request)
        print("The response of OrdersApi->create_orders_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->create_orders_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_orders_request** | [**CreateOrdersRequest**](CreateOrdersRequest.md)|  | 

### Return type

[**CreateOrdersResponse**](CreateOrdersResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request Processed Successfully |  -  |
**400** | Bad Request (Request has missing or invalid parameters and cannot be parsed) |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_orders_async**
> DeleteOrdersResource delete_orders_async(order_identifiers)

Delete orders

Please be aware labels generated on orders which are deleted are no longer valid and must be destroyed.

Cancelled label information is automatically shared with Royal Mail Revenue Protection, and should
a cancelled label be identified on an item in the Royal Mail Network, you will be charged on your account
and an additional handling fee applied.


### Example

* Api Key Authentication (Bearer):

```python
import royal_mail_click_and_drop
from royal_mail_click_and_drop import DeleteOrdersResource
from royal_mail_click_and_drop import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = royal_mail_click_and_drop.Configuration(
    host="/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with royal_mail_click_and_drop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = royal_mail_click_and_drop.OrdersApi(api_client)
    order_identifiers = '/orders/\"ref\";1001;\"Reference%3BWith%3BSpecial%3BSymbols!\";2345/'  # str | One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.

    try:
        # Delete orders
        api_response = api_instance.delete_orders_async(order_identifiers)
        print("The response of OrdersApi->delete_orders_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->delete_orders_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_identifiers** | **str**| One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. | 

### Return type

[**DeleteOrdersResource**](DeleteOrdersResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provides a list of deleted orders references and ids and errors for orders that failed to delete |  -  |
**400** | Bad Request (Request has missing or invalid parameters and cannot be parsed) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (Feature not available) |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_async**
> GetOrdersResponse get_orders_async(page_size=page_size, start_date_time=start_date_time, end_date_time=end_date_time, continuation_token=continuation_token)

Retrieve pageable list of orders

### Example

* Api Key Authentication (Bearer):

```python
import royal_mail_click_and_drop
from royal_mail_click_and_drop.models.get_orders_response import GetOrdersResponse
from royal_mail_click_and_drop import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = royal_mail_click_and_drop.Configuration(
    host="/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with royal_mail_click_and_drop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = royal_mail_click_and_drop.OrdersApi(api_client)
    page_size = 25  # int | The number of items to return (optional) (default to 25)
    start_date_time = '2013-10-20T19:20:30+01:00'  # datetime | Date and time lower bound for items filtering (optional)
    end_date_time = '2013-10-20T19:20:30+01:00'  # datetime | Date and time upper bound for items filtering (optional)
    continuation_token = 'continuation_token_example'  # str | The token for retrieving the next page of items (optional)

    try:
        # Retrieve pageable list of orders
        api_response = api_instance.get_orders_async(
            page_size=page_size,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            continuation_token=continuation_token
        )
        print("The response of OrdersApi->get_orders_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orders_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items to return | [optional] [default to 25]
 **start_date_time** | **datetime**| Date and time lower bound for items filtering | [optional] 
 **end_date_time** | **datetime**| Date and time upper bound for items filtering | [optional] 
 **continuation_token** | **str**| The token for retrieving the next page of items | [optional] 

### Return type

[**GetOrdersResponse**](GetOrdersResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return pageable list of orders |  -  |
**400** | Bad Request (Request has missing or invalid parameters and cannot be parsed) |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_with_details_async**
> GetOrdersDetailsResponse get_orders_with_details_async(page_size=page_size, start_date_time=start_date_time, end_date_time=end_date_time, continuation_token=continuation_token)

Retrieve pageable list of orders with details

<b>Reserved for ChannelShipper customers only - please visit <a href="https://channelshipper.com/" target="_self">ChannelShipper.com</a> for more information</b>

### Example

* Api Key Authentication (Bearer):

```python
import royal_mail_click_and_drop
from royal_mail_click_and_drop import GetOrdersDetailsResponse
from royal_mail_click_and_drop import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = royal_mail_click_and_drop.Configuration(
    host="/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with royal_mail_click_and_drop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = royal_mail_click_and_drop.OrdersApi(api_client)
    page_size = 25  # int | The number of items to return (optional) (default to 25)
    start_date_time = '2013-10-20T19:20:30+01:00'  # datetime | Date and time lower bound for items filtering (optional)
    end_date_time = '2013-10-20T19:20:30+01:00'  # datetime | Date and time upper bound for items filtering (optional)
    continuation_token = 'continuation_token_example'  # str | The token for retrieving the next page of items (optional)

    try:
        # Retrieve pageable list of orders with details
        api_response = api_instance.get_orders_with_details_async(
            page_size=page_size,
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            continuation_token=continuation_token
        )
        print("The response of OrdersApi->get_orders_with_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orders_with_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| The number of items to return | [optional] [default to 25]
 **start_date_time** | **datetime**| Date and time lower bound for items filtering | [optional] 
 **end_date_time** | **datetime**| Date and time upper bound for items filtering | [optional] 
 **continuation_token** | **str**| The token for retrieving the next page of items | [optional] 

### Return type

[**GetOrdersDetailsResponse**](GetOrdersDetailsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return a pageable list of orders with details |  -  |
**400** | Bad Request (Request has missing or invalid parameters and cannot be parsed) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (Feature not available) |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_orders_async**
> List[GetOrderInfoResource] get_specific_orders_async(order_identifiers)

Retrieve specific orders

### Example

* Api Key Authentication (Bearer):

```python
import royal_mail_click_and_drop
from royal_mail_click_and_drop import GetOrderInfoResource
from royal_mail_click_and_drop import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = royal_mail_click_and_drop.Configuration(
    host="/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with royal_mail_click_and_drop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = royal_mail_click_and_drop.OrdersApi(api_client)
    order_identifiers = '/orders/\"ref\";1001;\"Reference%3BWith%3BSpecial%3BSymbols!\";2345/'  # str | One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.

    try:
        # Retrieve specific orders
        api_response = api_instance.get_specific_orders_async(order_identifiers)
        print("The response of OrdersApi->get_specific_orders_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_specific_orders_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_identifiers** | **str**| One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. | 

### Return type

[**List[GetOrderInfoResource]**](GetOrderInfoResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return list of specific orders |  -  |
**400** | Bad Request (Request has missing or invalid parameters and cannot be parsed) |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_orders_with_details_async**
> List[GetOrderDetailsResource] get_specific_orders_with_details_async(order_identifiers)

Retrieve details of the specific orders

<b>Reserved for ChannelShipper customers only - please visit <a href="https://channelshipper.com/" target="_self">ChannelShipper.com</a> for more information</b>

### Example

* Api Key Authentication (Bearer):

```python
import royal_mail_click_and_drop
from royal_mail_click_and_drop import GetOrderDetailsResource
from royal_mail_click_and_drop import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = royal_mail_click_and_drop.Configuration(
    host="/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with royal_mail_click_and_drop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = royal_mail_click_and_drop.OrdersApi(api_client)
    order_identifiers = '/orders/\"ref\";1001;\"Reference%3BWith%3BSpecial%3BSymbols!\";2345/'  # str | One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.

    try:
        # Retrieve details of the specific orders
        api_response = api_instance.get_specific_orders_with_details_async(order_identifiers)
        print("The response of OrdersApi->get_specific_orders_with_details_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_specific_orders_with_details_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_identifiers** | **str**| One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. | 

### Return type

[**List[GetOrderDetailsResource]**](GetOrderDetailsResource.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return detailed information about the orders |  -  |
**400** | Bad Request (Request has missing or invalid parameters and cannot be parsed) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (Feature not available) |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_orders_status_async**
> UpdateOrderStatusResponse update_orders_status_async(update_orders_status_request)

Set order status

### Example

* Api Key Authentication (Bearer):

```python
import royal_mail_click_and_drop
from royal_mail_click_and_drop.models.update_order_status_response import UpdateOrderStatusResponse
from royal_mail_click_and_drop import UpdateOrdersStatusRequest
from royal_mail_click_and_drop import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = royal_mail_click_and_drop.Configuration(
    host="/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with royal_mail_click_and_drop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = royal_mail_click_and_drop.OrdersApi(api_client)
    update_orders_status_request = royal_mail_click_and_drop.UpdateOrdersStatusRequest()  # UpdateOrdersStatusRequest | At least one of 'orderIdentifier' and 'orderReference' is required. Providing both is disallowed to avoid ambiguity.  When the status is set to 'despatchedByOtherCourier', if the optional parameter 'trackingNumber' is provided then the parameters 'despatchDate', 'shippingCarrier' and 'shippingService' are also required. The maximum collection length is 100. 

    try:
        # Set order status
        api_response = api_instance.update_orders_status_async(update_orders_status_request)
        print("The response of OrdersApi->update_orders_status_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->update_orders_status_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_orders_status_request** | [**UpdateOrdersStatusRequest**](UpdateOrdersStatusRequest.md)| At least one of &#39;orderIdentifier&#39; and &#39;orderReference&#39; is required. Providing both is disallowed to avoid ambiguity.  When the status is set to &#39;despatchedByOtherCourier&#39;, if the optional parameter &#39;trackingNumber&#39; is provided then the parameters &#39;despatchDate&#39;, &#39;shippingCarrier&#39; and &#39;shippingService&#39; are also required. The maximum collection length is 100.  | 

### Return type

[**UpdateOrderStatusResponse**](UpdateOrderStatusResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Provides a list of orders |  -  |
**400** | Bad Request (Request has missing or invalid parameters and cannot be parsed) |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

