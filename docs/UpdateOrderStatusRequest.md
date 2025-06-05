# UpdateOrderStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_identifier** | **int** |  | [optional] 
**order_reference** | **str** |  | [optional] 
**status** | **str** | &lt;br/&gt; \&quot;&lt;i&gt;despatchedByOtherCourier&lt;/i&gt; \&quot;: &lt;b&gt;Reserved for ChannelShipper customers only - please visit &lt;a href&#x3D;\&quot;https://channelshipper.com/\&quot; target&#x3D;\&quot;_self\&quot;&gt;ChannelShipper.com&lt;/a&gt; for more information&lt;/b&gt;  \&quot;&lt;i&gt;new&lt;/i&gt; \&quot;: This will remove the order from its batch. Order information will not be lost during this process.  Please be aware labels generated on orders which are then set to \&quot;new\&quot; (reset) are no longer valid and must be destroyed. If the order is required to be despatched after setting to \&quot;new\&quot; status, a new label must be generated to attach to the item.  Cancelled label information is automatically shared with Royal Mail Revenue Protection, and should a cancelled label be identified on an item in the Royal Mail Network, you will be charged on your account and an additional handling fee applied.  | [optional] 
**tracking_number** | **str** |  | [optional] 
**despatch_date** | **datetime** |  | [optional] 
**shipping_carrier** | **str** |  | [optional] 
**shipping_service** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_order_status_request import UpdateOrderStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrderStatusRequest from a JSON string
update_order_status_request_instance = UpdateOrderStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrderStatusRequest.to_json())

# convert the object into a dict
update_order_status_request_dict = update_order_status_request_instance.to_dict()
# create an instance of UpdateOrderStatusRequest from a dict
update_order_status_request_from_dict = UpdateOrderStatusRequest.from_dict(update_order_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


