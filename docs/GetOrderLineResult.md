# GetOrderLineResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**quantity** | **int** | The number of units in a given line | 
**unit_value** | **float** | The price of a single unit excluding tax | [optional] 
**line_total** | **float** | The sum of the line items including tax | [optional] 
**customs_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_order_line_result import GetOrderLineResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderLineResult from a JSON string
get_order_line_result_instance = GetOrderLineResult.from_json(json)
# print the JSON string representation of the object
print(GetOrderLineResult.to_json())

# convert the object into a dict
get_order_line_result_dict = get_order_line_result_instance.to_dict()
# create an instance of GetOrderLineResult from a dict
get_order_line_result_from_dict = GetOrderLineResult.from_dict(get_order_line_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


