# openapi_client.ManifestsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_manifest_async**](ManifestsApi.md#get_manifest_async) | **GET** /manifests/{manifestIdentifier} | Get manifest
[**manifest_eligible_async**](ManifestsApi.md#manifest_eligible_async) | **POST** /manifests | Manifest eligible orders
[**retry_manifest_async**](ManifestsApi.md#retry_manifest_async) | **POST** /manifests/retry/{manifestIdentifier} | Retry manifest


# **get_manifest_async**
> ManifestDetailsResponse get_manifest_async(manifest_identifier)

Get manifest

Retrieve manifest paperwork for a previously successful ‘Manifest eligible orders’ endpoint call

### Example

* Api Key Authentication (Bearer):

```python
import royal_mail_click_and_drop
from royal_mail_click_and_drop import ManifestDetailsResponse
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
    api_instance = royal_mail_click_and_drop.ManifestsApi(api_client)
    manifest_identifier = 12345  # int | The manifest number returned from the initial ‘Manifest eligible orders’ endpoint call

    try:
        # Get manifest
        api_response = api_instance.get_manifest_async(manifest_identifier)
        print("The response of ManifestsApi->get_manifest_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestsApi->get_manifest_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_identifier** | **int**| The manifest number returned from the initial ‘Manifest eligible orders’ endpoint call | 

### Return type

[**ManifestDetailsResponse**](ManifestDetailsResponse.md)

### Authorization

[Bearer](../README_AUTO.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Get Manifest request was successfully processed. The manifest details were retrieved, but the Printable PDF Manifest may or may not be available at this time. Please try the Get Manifest endpoint. If it is not available after a reasonable period, please &lt;a href&#x3D;&#39;https://help.parcel.royalmail.com/hc/en-gb/articles/115003806094-Contact-Support&#39; target&#x3D;&#39;_self&#39;&gt;contact support&lt;/a&gt; for assistance.  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (Feature not available) |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to README]](../README_AUTO.md)

# **manifest_eligible_async**
> ManifestOrdersResponse manifest_eligible_async()

Manifest eligible orders

Manifest all orders in 'Label Generated' and 'Despatched' statuses and return manifest paperwork where possible

### Example

* Api Key Authentication (Bearer):

```python
import royal_mail_click_and_drop
from royal_mail_click_and_drop import ManifestOrdersResponse
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
    api_instance = royal_mail_click_and_drop.ManifestsApi(api_client)

    try:
        # Manifest eligible orders
        api_response = api_instance.manifest_eligible_async()
        print("The response of ManifestsApi->manifest_eligible_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestsApi->manifest_eligible_async: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ManifestOrdersResponse**](ManifestOrdersResponse.md)

### Authorization

[Bearer](../README_AUTO.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Manifest all eligible orders request was successful, and a manifest has been created. The Printable PDF manifest is available for download.  |  -  |
**202** | The Manifest eligible orders request was successful, and a manifest has been created. However, the printable manifest PDF is not yet available. The printable manifest PDF should be accessible later via the Get Manifest endpoint. If it is not available after a reasonable period, please &lt;a href&#x3D;&#39;https://help.parcel.royalmail.com/hc/en-gb/articles/115003806094-Contact-Support&#39; target&#x3D;&#39;_self&#39;&gt;contact support&lt;/a&gt; for assistance.  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (Feature not available) |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to README]](../README_AUTO.md)

# **retry_manifest_async**
> ManifestOrdersResponse retry_manifest_async(manifest_identifier)

Retry manifest

Retry a manifest operation if the eligible orders were not able to be successfully processed in the initial ‘Manifest eligible orders’ endpoint call and return manifest paperwork where possible


### Example

* Api Key Authentication (Bearer):

```python
import royal_mail_click_and_drop
from royal_mail_click_and_drop import ManifestOrdersResponse
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
    api_instance = royal_mail_click_and_drop.ManifestsApi(api_client)
    manifest_identifier = 12345  # int | The manifest number returned from the initial ‘Manifest eligible orders’ endpoint call

    try:
        # Retry manifest
        api_response = api_instance.retry_manifest_async(manifest_identifier)
        print("The response of ManifestsApi->retry_manifest_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManifestsApi->retry_manifest_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_identifier** | **int**| The manifest number returned from the initial ‘Manifest eligible orders’ endpoint call | 

### Return type

[**ManifestOrdersResponse**](ManifestOrdersResponse.md)

### Authorization

[Bearer](../README_AUTO.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The Retry Manifest request was successful, and a manifest has been created. The printable manifest PDF is available for download. |  -  |
**202** | The retry request was successfully processed, and a manifest has been created, but the documentation is not yet available. The manifest should be accessible later via the Get Manifest endpoint.  If it is not available after a reasonable period, please &lt;a href&#x3D;&#39;https://help.parcel.royalmail.com/hc/en-gb/articles/115003806094-Contact-Support&#39; target&#x3D;&#39;_self&#39;&gt;contact support&lt;/a&gt; for assistance.  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (Feature not available) |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to README]](../README_AUTO.md)

