# FailedOrderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | [**CreateOrderRequest**](CreateOrderRequest.md) |  | [optional] 
**errors** | [**List[CreateOrderErrorResponse]**](CreateOrderErrorResponse.md) |  | [optional] 

## Example

```python
from royal_mail_click_and_drop import FailedOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FailedOrderResponse from a JSON string
failed_order_response_instance = FailedOrderResponse.from_json(json)
# print the JSON string representation of the object
print(FailedOrderResponse.to_json())

# convert the object into a dict
failed_order_response_dict = failed_order_response_instance.to_dict()
# create an instance of FailedOrderResponse from a dict
failed_order_response_from_dict = FailedOrderResponse.from_dict(failed_order_response_dict)
```
[[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to README]](../README_AUTO.md)


