# GetOrderInfoResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_identifier** | **int** |  | 
**order_reference** | **str** |  | [optional] 
**created_on** | **datetime** |  | 
**order_date** | **datetime** |  | [optional] 
**printed_on** | **datetime** |  | [optional] 
**manifested_on** | **datetime** |  | [optional] 
**shipped_on** | **datetime** |  | [optional] 
**tracking_number** | **str** |  | [optional] 

## Example

```python
from royal_mail_click_and_drop import GetOrderInfoResource

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderInfoResource from a JSON string
get_order_info_resource_instance = GetOrderInfoResource.from_json(json)
# print the JSON string representation of the object
print(GetOrderInfoResource.to_json())

# convert the object into a dict
get_order_info_resource_dict = get_order_info_resource_instance.to_dict()
# create an instance of GetOrderInfoResource from a dict
get_order_info_resource_from_dict = GetOrderInfoResource.from_dict(get_order_info_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


