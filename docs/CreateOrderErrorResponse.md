# CreateOrderErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**fields** | [**List[OrderFieldResponse]**](OrderFieldResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_order_error_response import CreateOrderErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderErrorResponse from a JSON string
create_order_error_response_instance = CreateOrderErrorResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrderErrorResponse.to_json())

# convert the object into a dict
create_order_error_response_dict = create_order_error_response_instance.to_dict()
# create an instance of CreateOrderErrorResponse from a dict
create_order_error_response_from_dict = CreateOrderErrorResponse.from_dict(create_order_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


