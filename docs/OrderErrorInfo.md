# OrderErrorInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_identifier** | **int** |  | [optional] 
**order_reference** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.order_error_info import OrderErrorInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderErrorInfo from a JSON string
order_error_info_instance = OrderErrorInfo.from_json(json)
# print the JSON string representation of the object
print(OrderErrorInfo.to_json())

# convert the object into a dict
order_error_info_dict = order_error_info_instance.to_dict()
# create an instance of OrderErrorInfo from a dict
order_error_info_from_dict = OrderErrorInfo.from_dict(order_error_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


