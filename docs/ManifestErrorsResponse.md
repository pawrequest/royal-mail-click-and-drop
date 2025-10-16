# ManifestErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ManifestErrorsErrorDetailsResponse]**](ManifestErrorsErrorDetailsResponse.md) |  | [optional] 

## Example

```python
from royal_mail_click_and_drop import ManifestErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestErrorsResponse from a JSON string
manifest_errors_response_instance = ManifestErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(ManifestErrorsResponse.to_json())

# convert the object into a dict
manifest_errors_response_dict = manifest_errors_response_instance.to_dict()
# create an instance of ManifestErrorsResponse from a dict
manifest_errors_response_from_dict = ManifestErrorsResponse.from_dict(manifest_errors_response_dict)
```
[[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to README]](../README_AUTO.md)


