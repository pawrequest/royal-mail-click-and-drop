# UpdatedOrderInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_identifier** | **int** |  | [optional] 
**order_reference** | **str** |  | [optional] 
**status** | **str** | Current status of the order | [optional] 

## Example

```python
from openapi_client.models.updated_order_info import UpdatedOrderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatedOrderInfo from a JSON string
updated_order_info_instance = UpdatedOrderInfo.from_json(json)
# print the JSON string representation of the object
print(UpdatedOrderInfo.to_json())

# convert the object into a dict
updated_order_info_dict = updated_order_info_instance.to_dict()
# create an instance of UpdatedOrderInfo from a dict
updated_order_info_from_dict = UpdatedOrderInfo.from_dict(updated_order_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


