# CreateOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CreateOrderRequest]**](CreateOrderRequest.md) |  | 

## Example

```python
from royal_mail_click_and_drop import CreateOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrdersRequest from a JSON string
create_orders_request_instance = CreateOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrdersRequest.to_json())

# convert the object into a dict
create_orders_request_dict = create_orders_request_instance.to_dict()
# create an instance of CreateOrdersRequest from a dict
create_orders_request_from_dict = CreateOrdersRequest.from_dict(create_orders_request_dict)
```
[[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to README]](../README_AUTO.md)


