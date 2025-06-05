# DimensionsRequest

It is not mandatory to include the dimensions field. If the dimensions field is included then the inner fields heightInMms, widthInMms and depthInMms must be specified with non-zero values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height_in_mms** | **int** |  | 
**width_in_mms** | **int** |  | 
**depth_in_mms** | **int** |  | 

## Example

```python
from openapi_client.models.dimensions_request import DimensionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionsRequest from a JSON string
dimensions_request_instance = DimensionsRequest.from_json(json)
# print the JSON string representation of the object
print(DimensionsRequest.to_json())

# convert the object into a dict
dimensions_request_dict = dimensions_request_instance.to_dict()
# create an instance of DimensionsRequest from a dict
dimensions_request_from_dict = DimensionsRequest.from_dict(dimensions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


