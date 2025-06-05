# ProductItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**sku** | **str** | The presence or not of field &lt;b&gt;SKU&lt;/b&gt; and other fields in the request body will determine which of the following behaviours occur:- &lt;br&gt;1) A minimum of &lt;b&gt;SKU&lt;/b&gt;, &lt;b&gt;unitValue&lt;/b&gt;, &lt;b&gt;unitWeightInGrams&lt;/b&gt; and &lt;b&gt;quantity&lt;/b&gt; provided - In addition to the provided product fields being used for the order creation, an existing account Product with matching SKU will be overwritten with all provided product parameters. If no existing account Product with matching SKU can be found then a new product will be created with the provided SKU and product parameters.&lt;br&gt;2) &lt;b&gt;SKU&lt;/b&gt;, &lt;b&gt;quantity&lt;/b&gt; provided and &lt;b&gt;no other fields&lt;/b&gt; provided - An account Product with the provided SKU will be used for the order if it exists.&lt;br&gt;3) &lt;b&gt;SKU not provided&lt;/b&gt; and a minimum of &lt;b&gt;unitValue&lt;/b&gt;, &lt;b&gt;unitWeightInGrams&lt;/b&gt; and &lt;b&gt;quantity&lt;/b&gt; provided - All provided product fields will be used for the order creation.&lt;br&gt;4) All other scenarios will result in a validation error. | [optional] 
**quantity** | **int** | The number of units in a given line | 
**unit_value** | **float** | The price of a single unit excluding tax | [optional] 
**unit_weight_in_grams** | **int** |  | [optional] 
**customs_description** | **str** |  | [optional] 
**extended_customs_description** | **str** |  | [optional] 
**customs_code** | **str** |  | [optional] 
**origin_country_code** | **str** |  | [optional] 
**customs_declaration_category** | **str** |  | [optional] 
**requires_export_licence** | **bool** |  | [optional] 
**stock_location** | **str** |  | [optional] 
**use_origin_preference** | **bool** |  | [optional] 
**supplementary_units** | **str** |  | [optional] 
**license_number** | **str** |  | [optional] 
**certificate_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.product_item_request import ProductItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductItemRequest from a JSON string
product_item_request_instance = ProductItemRequest.from_json(json)
# print the JSON string representation of the object
print(ProductItemRequest.to_json())

# convert the object into a dict
product_item_request_dict = product_item_request_instance.to_dict()
# create an instance of ProductItemRequest from a dict
product_item_request_from_dict = ProductItemRequest.from_dict(product_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


