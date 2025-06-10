# openapi_client.VersionApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_version_async**](VersionApi.md#get_version_async) | **GET** /version | Get API version details.


# **get_version_async**
> GetVersionResource get_version_async()

Get API version details.

### Example

```python
import royal_mail_click_and_drop
from royal_mail_click_and_drop import GetVersionResource
from royal_mail_click_and_drop import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = royal_mail_click_and_drop.Configuration(
    host="/api/v1"
)

# Enter a context with an instance of the API client
with royal_mail_click_and_drop.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = royal_mail_click_and_drop.VersionApi(api_client)

    try:
        # Get API version details.
        api_response = api_instance.get_version_async()
        print("The response of VersionApi->get_version_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionApi->get_version_async: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetVersionResource**](GetVersionResource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns details about the API version |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

