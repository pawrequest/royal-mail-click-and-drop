# SenderDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_name** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sender_details_request import SenderDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SenderDetailsRequest from a JSON string
sender_details_request_instance = SenderDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(SenderDetailsRequest.to_json())

# convert the object into a dict
sender_details_request_dict = sender_details_request_instance.to_dict()
# create an instance of SenderDetailsRequest from a dict
sender_details_request_from_dict = SenderDetailsRequest.from_dict(sender_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


