# openapi_client.LabelsApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_orders_label_async**](LabelsApi.md#get_orders_label_async) | **GET** /orders/{orderIdentifiers}/label | Return a single PDF file with generated label and/or associated document(s)


# **get_orders_label_async**
> bytearray get_orders_label_async(order_identifiers, document_type, include_returns_label=include_returns_label, include_cn=include_cn)

Return a single PDF file with generated label and/or associated document(s)

<b>Reserved for OBA customers only</b>

The account "Label format" settings page will control the page format settings used to print the postage label
and associated documents. Certain combinations of these settings may prevent associated documents from being
printed together with the postage label within a single document. If this occurs the documentType option can be
used in a separate call to print missing documents.


### Example

* Api Key Authentication (Bearer):

```python
import royal_mail_click_and_drop
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
    api_instance = royal_mail_click_and_drop.LabelsApi(api_client)
    order_identifiers = '/orders/\"ref\";1001;\"Reference%3BWith%3BSpecial%3BSymbols!\";2345/'  # str | One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100.
    document_type = 'document_type_example'  # str | Document generation mode. When documentType is set to \"postageLabel\" the additional parameters below must be used. These additional parameters will be ignored when documentType is not set to \"postageLabel\"
    include_returns_label = True  # bool | Include returns label. Required when documentType is set to 'postageLabel' (optional)
    include_cn = True  # bool | Include CN22/CN23 with label. Optional parameter. If this parameter is used the setting will override the default account behaviour specified in the \"Label format\" setting \"Generate customs declarations with orders\" (optional)

    try:
        # Return a single PDF file with generated label and/or associated document(s)
        api_response = api_instance.get_orders_label_async(
            order_identifiers,
            document_type,
            include_returns_label=include_returns_label,
            include_cn=include_cn
        )
        print("The response of LabelsApi->get_orders_label_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->get_orders_label_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_identifiers** | **str**| One or several Order Identifiers or Order References separated by semicolon. Order Identifiers are integer numbers. Order References are strings - each must be percent-encoded and surrounded by double quotation marks. The maximum number of identifiers is 100. | 
 **document_type** | **str**| Document generation mode. When documentType is set to \&quot;postageLabel\&quot; the additional parameters below must be used. These additional parameters will be ignored when documentType is not set to \&quot;postageLabel\&quot; | 
 **include_returns_label** | **bool**| Include returns label. Required when documentType is set to &#39;postageLabel&#39; | [optional] 
 **include_cn** | **bool**| Include CN22/CN23 with label. Optional parameter. If this parameter is used the setting will override the default account behaviour specified in the \&quot;Label format\&quot; setting \&quot;Generate customs declarations with orders\&quot; | [optional] 

### Return type

**bytearray**

### Authorization

[Bearer](../README_AUTO.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return the PDF file with labels |  -  |
**400** | Bad Request (Request has missing or invalid parameters and cannot be parsed) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (Feature available for OBA accounts only) |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to README]](../README_AUTO.md)

