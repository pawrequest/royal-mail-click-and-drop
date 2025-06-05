# Importer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_name** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**address_line3** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**postcode** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**business_name** | **str** |  | [optional] 
**contact_name** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**tax_code** | **str** |  | [optional] 
**eori_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.importer import Importer

# TODO update the JSON string below
json = "{}"
# create an instance of Importer from a JSON string
importer_instance = Importer.from_json(json)
# print the JSON string representation of the object
print(Importer.to_json())

# convert the object into a dict
importer_dict = importer_instance.to_dict()
# create an instance of Importer from a dict
importer_from_dict = Importer.from_dict(importer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


