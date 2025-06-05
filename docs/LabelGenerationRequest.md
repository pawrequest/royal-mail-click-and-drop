# LabelGenerationRequest

<b>Reserved for OBA customers only</b>

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_label_in_response** | **bool** |  | 
**include_cn** | **bool** |  | [optional] 
**include_returns_label** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.label_generation_request import LabelGenerationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LabelGenerationRequest from a JSON string
label_generation_request_instance = LabelGenerationRequest.from_json(json)
# print the JSON string representation of the object
print(LabelGenerationRequest.to_json())

# convert the object into a dict
label_generation_request_dict = label_generation_request_instance.to_dict()
# create an instance of LabelGenerationRequest from a dict
label_generation_request_from_dict = LabelGenerationRequest.from_dict(label_generation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


