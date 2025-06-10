# CreateOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_identifier** | **int** |  | 
**order_reference** | **str** |  | [optional] 
**created_on** | **datetime** |  | 
**order_date** | **datetime** |  | [optional] 
**printed_on** | **datetime** |  | [optional] 
**manifested_on** | **datetime** |  | [optional] 
**shipped_on** | **datetime** |  | [optional] 
**tracking_number** | **str** |  | [optional] 
**label** | **str** | label in format base64 string | [optional] 
**label_errors** | [**List[CreateOrderLabelErrorResponse]**](CreateOrderLabelErrorResponse.md) |  | [optional] 
**generated_documents** | **List[str]** |  | [optional] 

## Example

```python
from royal_mail_click_and_drop import CreateOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderResponse from a JSON string
create_order_response_instance = CreateOrderResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrderResponse.to_json())

# convert the object into a dict
create_order_response_dict = create_order_response_instance.to_dict()
# create an instance of CreateOrderResponse from a dict
create_order_response_from_dict = CreateOrderResponse.from_dict(create_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


