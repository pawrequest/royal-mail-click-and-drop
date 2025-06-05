# UpdateOrderStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_orders** | [**List[UpdatedOrderInfo]**](UpdatedOrderInfo.md) |  | [optional] 
**errors** | [**List[OrderUpdateError]**](OrderUpdateError.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_order_status_response import UpdateOrderStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderStatusResponse from a JSON string
update_order_status_response_instance = UpdateOrderStatusResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderStatusResponse.to_json())

# convert the object into a dict
update_order_status_response_dict = update_order_status_response_instance.to_dict()
# create an instance of UpdateOrderStatusResponse from a dict
update_order_status_response_from_dict = UpdateOrderStatusResponse.from_dict(update_order_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


