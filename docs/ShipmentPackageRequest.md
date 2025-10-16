# ShipmentPackageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weight_in_grams** | **int** |  | 
**package_format_identifier** | **str** | &lt;b&gt;If you have a ChannelShipper account, you can also pass the name of any of your custom package formats instead of the values below.&lt;/b&gt;&lt;br&gt; Enum: &#39;undefined&#39;, &#39;letter&#39;, &#39;largeLetter&#39;, &#39;smallParcel&#39;, &#39;mediumParcel&#39;, &#39;parcel&#39;, &#39;documents&#39; | 
**custom_package_format_identifier** | **str** | This field will be deprecated in the future. Please use &#39;packageFormatIdentifier&#39; for custom package formats from ChannelShipper. | [optional] 
**dimensions** | [**DimensionsRequest**](DimensionsRequest.md) |  | [optional] 
**contents** | [**List[ProductItemRequest]**](ProductItemRequest.md) |  | [optional] 

## Example

```python
from royal_mail_click_and_drop import ShipmentPackageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentPackageRequest from a JSON string
shipment_package_request_instance = ShipmentPackageRequest.from_json(json)
# print the JSON string representation of the object
print(ShipmentPackageRequest.to_json())

# convert the object into a dict
shipment_package_request_dict = shipment_package_request_instance.to_dict()
# create an instance of ShipmentPackageRequest from a dict
shipment_package_request_from_dict = ShipmentPackageRequest.from_dict(shipment_package_request_dict)
```
[[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to README]](../README_AUTO.md)


