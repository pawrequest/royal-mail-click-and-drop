# CreateOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_reference** | **str** |  | [optional] 
**is_recipient_a_business** | **bool** | Indicates if the recipient is a business or not. Mandatory for Business senders on orders shipping from Great Britain to Northern Ireland, which require additional information for B2B shipments. (Business senders are OBA accounts and OLP accounts declaring themselves as a Business sender). | [optional] 
**recipient** | [**RecipientDetailsRequest**](RecipientDetailsRequest.md) |  | 
**sender** | [**SenderDetailsRequest**](SenderDetailsRequest.md) |  | [optional] 
**billing** | [**BillingDetailsRequest**](BillingDetailsRequest.md) |  | [optional] 
**packages** | [**List[ShipmentPackageRequest]**](ShipmentPackageRequest.md) |  | [optional] 
**order_date** | **datetime** |  | 
**planned_despatch_date** | **datetime** |  | [optional] 
**special_instructions** | **str** |  | [optional] 
**subtotal** | **float** | The total value of all the goods in the order, excluding tax. This should not include retail shipping costs | 
**shipping_cost_charged** | **float** | The shipping costs you charged to your customer | 
**other_costs** | **float** |  | [optional] 
**customs_duty_costs** | **float** | Customs Duty Costs is only supported in DDP (Delivery Duty Paid) services | [optional] 
**total** | **float** | The sum of order subtotal, tax and retail shipping costs | 
**currency_code** | **str** |  | [optional] 
**postage_details** | [**PostageDetailsRequest**](PostageDetailsRequest.md) |  | [optional] 
**tags** | [**List[TagRequest]**](TagRequest.md) |  | [optional] 
**label** | [**LabelGenerationRequest**](LabelGenerationRequest.md) |  | [optional] 
**order_tax** | **float** | The total tax charged for the order | [optional] 
**contains_dangerous_goods** | **bool** | Indicates that the package contents contain a dangerous goods item | [optional] 
**dangerous_goods_un_code** | **str** | UN Code of the dangerous goods | [optional] 
**dangerous_goods_description** | **float** | Description of the dangerous goods | [optional] 
**dangerous_goods_quantity** | **float** | Quantity or volume of the dangerous goods | [optional] 
**importer** | [**Importer**](Importer.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_order_request import CreateOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderRequest from a JSON string
create_order_request_instance = CreateOrderRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrderRequest.to_json())

# convert the object into a dict
create_order_request_dict = create_order_request_instance.to_dict()
# create an instance of CreateOrderRequest from a dict
create_order_request_from_dict = CreateOrderRequest.from_dict(create_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


