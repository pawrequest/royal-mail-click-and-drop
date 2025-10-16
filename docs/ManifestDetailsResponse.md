# ManifestDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest_number** | **float** |  | 
**status** | **str** |  | [optional] 
**document_pdf** | **str** | manifest in format base64 string | [optional] 

## Example

```python
from royal_mail_click_and_drop import ManifestDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestDetailsResponse from a JSON string
manifest_details_response_instance = ManifestDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(ManifestDetailsResponse.to_json())

# convert the object into a dict
manifest_details_response_dict = manifest_details_response_instance.to_dict()
# create an instance of ManifestDetailsResponse from a dict
manifest_details_response_from_dict = ManifestDetailsResponse.from_dict(manifest_details_response_dict)
```
[[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to README]](../README_AUTO.md)


