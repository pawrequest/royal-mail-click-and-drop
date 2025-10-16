# GetOrdersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[GetOrderInfoResource]**](GetOrderInfoResource.md) |  | [optional] 
**continuation_token** | **str** |  | [optional] 

## Example

```python
from royal_mail_click_and_drop.models.get_orders_response import GetOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrdersResponse from a JSON string
get_orders_response_instance = GetOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(GetOrdersResponse.to_json())

# convert the object into a dict
get_orders_response_dict = get_orders_response_instance.to_dict()
# create an instance of GetOrdersResponse from a dict
get_orders_response_from_dict = GetOrdersResponse.from_dict(get_orders_response_dict)
```
[[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to README]](../README_AUTO.md)


