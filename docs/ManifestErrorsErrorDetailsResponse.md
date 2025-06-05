# ManifestErrorsErrorDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.manifest_errors_error_details_response import ManifestErrorsErrorDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestErrorsErrorDetailsResponse from a JSON string
manifest_errors_error_details_response_instance = ManifestErrorsErrorDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(ManifestErrorsErrorDetailsResponse.to_json())

# convert the object into a dict
manifest_errors_error_details_response_dict = manifest_errors_error_details_response_instance.to_dict()
# create an instance of ManifestErrorsErrorDetailsResponse from a dict
manifest_errors_error_details_response_from_dict = ManifestErrorsErrorDetailsResponse.from_dict(manifest_errors_error_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


