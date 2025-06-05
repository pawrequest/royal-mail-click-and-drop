# ManifestOrdersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest_number** | **float** |  | 
**document_pdf** | **str** | manifest in format base64 string | [optional] 

## Example

```python
from openapi_client.models.manifest_orders_response import ManifestOrdersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestOrdersResponse from a JSON string
manifest_orders_response_instance = ManifestOrdersResponse.from_json(json)
# print the JSON string representation of the object
print(ManifestOrdersResponse.to_json())

# convert the object into a dict
manifest_orders_response_dict = manifest_orders_response_instance.to_dict()
# create an instance of ManifestOrdersResponse from a dict
manifest_orders_response_from_dict = ManifestOrdersResponse.from_dict(manifest_orders_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


