# UpdateOrdersStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UpdateOrderStatusRequest]**](UpdateOrderStatusRequest.md) |  | [optional] 

## Example

```python
from royal_mail_click_and_drop import UpdateOrdersStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrdersStatusRequest from a JSON string
update_orders_status_request_instance = UpdateOrdersStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrdersStatusRequest.to_json())

# convert the object into a dict
update_orders_status_request_dict = update_orders_status_request_instance.to_dict()
# create an instance of UpdateOrdersStatusRequest from a dict
update_orders_status_request_from_dict = UpdateOrdersStatusRequest.from_dict(update_orders_status_request_dict)
```
[[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to README]](../README_AUTO.md)


