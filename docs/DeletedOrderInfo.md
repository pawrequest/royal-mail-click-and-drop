# DeletedOrderInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_identifier** | **int** |  | [optional] 
**order_reference** | **str** |  | [optional] 
**order_info** | **str** |  | [optional] 

## Example

```python
from royal_mail_click_and_drop.models.deleted_order_info import DeletedOrderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedOrderInfo from a JSON string
deleted_order_info_instance = DeletedOrderInfo.from_json(json)
# print the JSON string representation of the object
print(DeletedOrderInfo.to_json())

# convert the object into a dict
deleted_order_info_dict = deleted_order_info_instance.to_dict()
# create an instance of DeletedOrderInfo from a dict
deleted_order_info_from_dict = DeletedOrderInfo.from_dict(deleted_order_info_dict)
```
[[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to README]](../README_AUTO.md)


