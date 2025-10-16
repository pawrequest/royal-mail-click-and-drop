# OrderErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_order_number** | **int** |  | [optional] 
**channel_order_reference** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from royal_mail_click_and_drop import OrderErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderErrorResponse from a JSON string
order_error_response_instance = OrderErrorResponse.from_json(json)
# print the JSON string representation of the object
print(OrderErrorResponse.to_json())

# convert the object into a dict
order_error_response_dict = order_error_response_instance.to_dict()
# create an instance of OrderErrorResponse from a dict
order_error_response_from_dict = OrderErrorResponse.from_dict(order_error_response_dict)
```
[[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to README]](../README_AUTO.md)


