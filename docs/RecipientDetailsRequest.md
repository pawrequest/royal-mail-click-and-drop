# RecipientDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**AddressRequest**](AddressRequest.md) |  | [optional] 
**phone_number** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**address_book_reference** | **str** | The presence or not of &lt;b&gt;addressBookReference&lt;/b&gt; and a valid &lt;b&gt;recipient address object&lt;/b&gt; in the request body will determine which of the following behaviours occur:-&lt;/br&gt;&lt;/br&gt;1) addressBookReference &lt;b&gt;provided&lt;/b&gt; and a valid recipient address object &lt;b&gt;provided&lt;/b&gt; - In addition to the provided recipient address fields being used for the order creation, an existing account Address Book Reference with matching addressBookReference will be overwritten with all provided recipient address fields, including phone and email. If no existing account Address Book Reference with matching addressBookReference can be found then a new one will be created with the provided addressBookReference and address fields, including phone and email.&lt;/br&gt;2) addressBookReference &lt;b&gt;provided&lt;/b&gt; and a valid recipient address object &lt;b&gt;not provided&lt;/b&gt; - An account Address Book Reference with the provided addressBookReference will be used for the order if it exists.&lt;/br&gt;3) addressBookReference &lt;b&gt;not provided&lt;/b&gt; and a valid recipient address object &lt;b&gt;provided&lt;/b&gt; - All provided recipient address fields, including phone and email, will be used for the order creation.&lt;/br&gt;4) All other scenarios will result in a validation error. | [optional] 

## Example

```python
from openapi_client.models.recipient_details_request import RecipientDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientDetailsRequest from a JSON string
recipient_details_request_instance = RecipientDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(RecipientDetailsRequest.to_json())

# convert the object into a dict
recipient_details_request_dict = recipient_details_request_instance.to_dict()
# create an instance of RecipientDetailsRequest from a dict
recipient_details_request_from_dict = RecipientDetailsRequest.from_dict(recipient_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


