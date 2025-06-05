# DeleteOrdersResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_orders** | [**List[DeletedOrderInfo]**](DeletedOrderInfo.md) |  | [optional] 
**errors** | [**List[OrderErrorInfo]**](OrderErrorInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.delete_orders_resource import DeleteOrdersResource

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOrdersResource from a JSON string
delete_orders_resource_instance = DeleteOrdersResource.from_json(json)
# print the JSON string representation of the object
print(DeleteOrdersResource.to_json())

# convert the object into a dict
delete_orders_resource_dict = delete_orders_resource_instance.to_dict()
# create an instance of DeleteOrdersResource from a dict
delete_orders_resource_from_dict = DeleteOrdersResource.from_dict(delete_orders_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


