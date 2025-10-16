# CreateOrdersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_count** | **int** |  | [optional] 
**errors_count** | **int** |  | [optional] 
**created_orders** | [**List[CreateOrderResponse]**](CreateOrderResponse.md) |  | [optional] 
**failed_orders** | [**List[FailedOrderResponse]**](FailedOrderResponse.md) |  | [optional] 

## Example

```python
from royal_mail_click_and_drop import CreateOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrdersResponse from a JSON string
create_orders_response_instance = CreateOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrdersResponse.to_json())

# convert the object into a dict
create_orders_response_dict = create_orders_response_instance.to_dict()
# create an instance of CreateOrdersResponse from a dict
create_orders_response_from_dict = CreateOrdersResponse.from_dict(create_orders_response_dict)
```
[[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to README]](../README_AUTO.md)


