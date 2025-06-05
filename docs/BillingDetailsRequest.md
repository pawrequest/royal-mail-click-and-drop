# BillingDetailsRequest

<b>Billing</b> along with <b>billing.address</b> objects are required in specific case when 'Use shipping address for billing address' setting is set to 'false' and 'Recipient.AddressBookReference' is provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**AddressRequest**](AddressRequest.md) |  | [optional] 
**phone_number** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.billing_details_request import BillingDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillingDetailsRequest from a JSON string
billing_details_request_instance = BillingDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(BillingDetailsRequest.to_json())

# convert the object into a dict
billing_details_request_dict = billing_details_request_instance.to_dict()
# create an instance of BillingDetailsRequest from a dict
billing_details_request_from_dict = BillingDetailsRequest.from_dict(billing_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


