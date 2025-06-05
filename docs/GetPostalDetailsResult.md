# GetPostalDetailsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**address_line3** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**county** | **str** |  | [optional] 
**postcode** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_postal_details_result import GetPostalDetailsResult

# TODO update the JSON string below
json = "{}"
# create an instance of GetPostalDetailsResult from a JSON string
get_postal_details_result_instance = GetPostalDetailsResult.from_json(json)
# print the JSON string representation of the object
print(GetPostalDetailsResult.to_json())

# convert the object into a dict
get_postal_details_result_dict = get_postal_details_result_instance.to_dict()
# create an instance of GetPostalDetailsResult from a dict
get_postal_details_result_from_dict = GetPostalDetailsResult.from_dict(get_postal_details_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


