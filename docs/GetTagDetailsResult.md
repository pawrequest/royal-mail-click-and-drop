# GetTagDetailsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_tag_details_result import GetTagDetailsResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetTagDetailsResult from a JSON string
get_tag_details_result_instance = GetTagDetailsResult.from_json(json)
# print the JSON string representation of the object
print(GetTagDetailsResult.to_json())

# convert the object into a dict
get_tag_details_result_dict = get_tag_details_result_instance.to_dict()
# create an instance of GetTagDetailsResult from a dict
get_tag_details_result_from_dict = GetTagDetailsResult.from_dict(get_tag_details_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


