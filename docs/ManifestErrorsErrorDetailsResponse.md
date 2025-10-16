# ManifestErrorsErrorDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from royal_mail_click_and_drop import ManifestErrorsErrorDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestErrorsErrorDetailsResponse from a JSON string
manifest_errors_error_details_response_instance = ManifestErrorsErrorDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(ManifestErrorsErrorDetailsResponse.to_json())

# convert the object into a dict
manifest_errors_error_details_response_dict = manifest_errors_error_details_response_instance.to_dict()
# create an instance of ManifestErrorsErrorDetailsResponse from a dict
manifest_errors_error_details_response_from_dict = ManifestErrorsErrorDetailsResponse.from_dict(
    manifest_errors_error_details_response_dict
)
```
[[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to README]](../README_AUTO.md)


