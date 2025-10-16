# CreateOrderLabelErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from royal_mail_click_and_drop import CreateOrderLabelErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrderLabelErrorResponse from a JSON string
create_order_label_error_response_instance = CreateOrderLabelErrorResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOrderLabelErrorResponse.to_json())

# convert the object into a dict
create_order_label_error_response_dict = create_order_label_error_response_instance.to_dict()
# create an instance of CreateOrderLabelErrorResponse from a dict
create_order_label_error_response_from_dict = CreateOrderLabelErrorResponse.from_dict(
    create_order_label_error_response_dict
)
```
[[Back to Model list]](../README_AUTO.md#documentation-for-models) [[Back to API list]](../README_AUTO.md#documentation-for-api-endpoints) [[Back to README]](../README_AUTO.md)


