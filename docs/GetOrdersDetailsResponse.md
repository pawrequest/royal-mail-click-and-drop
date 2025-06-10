# GetOrdersDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[GetOrderDetailsResource]**](GetOrderDetailsResource.md) |  | [optional] 
**continuation_token** | **str** |  | [optional] 

## Example

```python
from royal_mail_click_and_drop import GetOrdersDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrdersDetailsResponse from a JSON string
get_orders_details_response_instance = GetOrdersDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GetOrdersDetailsResponse.to_json())

# convert the object into a dict
get_orders_details_response_dict = get_orders_details_response_instance.to_dict()
# create an instance of GetOrdersDetailsResponse from a dict
get_orders_details_response_from_dict = GetOrdersDetailsResponse.from_dict(get_orders_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


