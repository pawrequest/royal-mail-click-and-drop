# OrderUpdateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_identifier** | **int** |  | [optional] 
**order_reference** | **str** |  | [optional] 
**status** | **str** | Current status of the order | [optional] 
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.order_update_error import OrderUpdateError

# TODO update the JSON string below
json = "{}"
# create an instance of OrderUpdateError from a JSON string
order_update_error_instance = OrderUpdateError.from_json(json)
# print the JSON string representation of the object
print(OrderUpdateError.to_json())

# convert the object into a dict
order_update_error_dict = order_update_error_instance.to_dict()
# create an instance of OrderUpdateError from a dict
order_update_error_from_dict = OrderUpdateError.from_dict(order_update_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


