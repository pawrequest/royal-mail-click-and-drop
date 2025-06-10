# GetTagDetailsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from royal_mail_click_and_drop import GetTagDetailsResult

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


