# OrderFieldResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.order_field_response import OrderFieldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrderFieldResponse from a JSON string
order_field_response_instance = OrderFieldResponse.from_json(json)
# print the JSON string representation of the object
print(OrderFieldResponse.to_json())

# convert the object into a dict
order_field_response_dict = order_field_response_instance.to_dict()
# create an instance of OrderFieldResponse from a dict
order_field_response_from_dict = OrderFieldResponse.from_dict(order_field_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


