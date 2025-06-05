# PostageDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_notifications_to** | **str** |  | [optional] 
**service_code** | **str** |  | [optional] 
**carrier_name** | **str** |  | [optional] 
**service_register_code** | **str** |  | [optional] 
**consequential_loss** | **int** |  | [optional] 
**receive_email_notification** | **bool** |  | [optional] 
**receive_sms_notification** | **bool** |  | [optional] 
**guaranteed_saturday_delivery** | **bool** | This field has been deprecated | [optional] 
**request_signature_upon_delivery** | **bool** |  | [optional] 
**is_local_collect** | **bool** |  | [optional] 
**safe_place** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**air_number** | **str** | For B2B orders shipping from Great Britain to Northern Ireland, this field can be used to provide the Recipient UKIMs number. | [optional] 
**ioss_number** | **str** |  | [optional] 
**requires_export_license** | **bool** |  | [optional] 
**commercial_invoice_number** | **str** |  | [optional] 
**commercial_invoice_date** | **datetime** |  | [optional] 
**recipient_eori_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.postage_details_request import PostageDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostageDetailsRequest from a JSON string
postage_details_request_instance = PostageDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(PostageDetailsRequest.to_json())

# convert the object into a dict
postage_details_request_dict = postage_details_request_instance.to_dict()
# create an instance of PostageDetailsRequest from a dict
postage_details_request_from_dict = PostageDetailsRequest.from_dict(postage_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


