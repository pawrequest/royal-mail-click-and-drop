# GetOrderDetailsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_identifier** | **int** |  | [optional] 
**order_status** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**printed_on** | **datetime** |  | [optional] 
**shipped_on** | **datetime** |  | [optional] 
**postage_applied_on** | **datetime** |  | [optional] 
**manifested_on** | **datetime** |  | [optional] 
**order_date** | **datetime** |  | [optional] 
**despatched_by_other_courier_on** | **datetime** |  | [optional] 
**trading_name** | **str** |  | [optional] 
**channel** | **str** |  | [optional] 
**marketplace_type_name** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**air_number** | **str** |  | [optional] 
**requires_export_license** | **bool** |  | [optional] 
**commercial_invoice_number** | **str** |  | [optional] 
**commercial_invoice_date** | **datetime** |  | [optional] 
**order_reference** | **str** |  | [optional] 
**channel_shipping_method** | **str** |  | [optional] 
**special_instructions** | **str** |  | [optional] 
**picker_special_instructions** | **str** |  | [optional] 
**subtotal** | **float** | The total value of all the goods in the order, excluding tax | 
**shipping_cost_charged** | **float** | The shipping costs you charged to your customer | 
**order_discount** | **float** |  | 
**total** | **float** | The sum of order subtotal, tax and retail shipping costs | 
**weight_in_grams** | **int** |  | 
**package_size** | **str** |  | [optional] 
**account_batch_number** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**shipping_details** | [**GetShippingDetailsResult**](GetShippingDetailsResult.md) |  | 
**shipping_info** | [**GetPostalDetailsResult**](GetPostalDetailsResult.md) |  | 
**billing_info** | [**GetPostalDetailsResult**](GetPostalDetailsResult.md) |  | 
**order_lines** | [**List[GetOrderLineResult]**](GetOrderLineResult.md) |  | 
**tags** | [**List[GetTagDetailsResult]**](GetTagDetailsResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_order_details_resource import GetOrderDetailsResource

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrderDetailsResource from a JSON string
get_order_details_resource_instance = GetOrderDetailsResource.from_json(json)
# print the JSON string representation of the object
print(GetOrderDetailsResource.to_json())

# convert the object into a dict
get_order_details_resource_dict = get_order_details_resource_instance.to_dict()
# create an instance of GetOrderDetailsResource from a dict
get_order_details_resource_from_dict = GetOrderDetailsResource.from_dict(get_order_details_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


