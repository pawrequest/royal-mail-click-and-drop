# GetShippingDetailsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_cost** | **float** |  | 
**tracking_number** | **str** |  | [optional] 
**shipping_tracking_status** | **str** |  | [optional] 
**service_code** | **str** |  | [optional] 
**shipping_service** | **str** |  | [optional] 
**shipping_carrier** | **str** |  | [optional] 
**receive_email_notification** | **bool** |  | [optional] 
**receive_sms_notification** | **bool** |  | [optional] 
**guaranteed_saturday_delivery** | **bool** |  | [optional] 
**request_signature_upon_delivery** | **bool** |  | [optional] 
**is_local_collect** | **bool** |  | [optional] 
**shipping_update_success_date** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.get_shipping_details_result import GetShippingDetailsResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetShippingDetailsResult from a JSON string
get_shipping_details_result_instance = GetShippingDetailsResult.from_json(json)
# print the JSON string representation of the object
print(GetShippingDetailsResult.to_json())

# convert the object into a dict
get_shipping_details_result_dict = get_shipping_details_result_instance.to_dict()
# create an instance of GetShippingDetailsResult from a dict
get_shipping_details_result_from_dict = GetShippingDetailsResult.from_dict(get_shipping_details_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


