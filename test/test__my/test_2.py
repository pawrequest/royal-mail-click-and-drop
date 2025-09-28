# import datetime
# import os
# from pprint import pprint
#
# from royal_mail_click_and_drop import (
#     AddressRequest,
#     ApiClient,
#     ApiException,
#     BillingDetailsRequest,
#     Configuration,
#     CreateOrdersRequest,
#     CreateOrdersResponse,
#     GetOrdersResponse,
#     LabelsApi,
#     ManifestOrdersResponse,
#     ManifestsApi,
#     OrdersApi,
#     RecipientDetailsRequest,
#     ShipmentPackageRequest,
#     VersionApi,
# )
# from royal_mail_click_and_drop.models import CreateOrderRequest
# from test__my.conftest import CONFIGURATION
#
#
# def test_get_version():
#     with ApiClient(CONFIGURATION) as rm:
#         client = VersionApi(rm)
#         try:
#             # api_response = inst.get_version_async()
#             response = client.get_version_async_with_http_info()
#             pprint(response.model_dump(), indent=4)
#         except ApiException as e:
#             print("ERROR")
#
#
#
# def recipient_():
#     return RecipientDetailsRequest(
#         address=recip_address(),
#         phone_number="07666666666",
#         email_address="sdgsdgsgd@sdgikhjbsdgijbsdigj.com",
#     )
#
#
# def billing_():
#     return BillingDetailsRequest(
#         address=our_address(),
#         phone_number="07878867844",
#         email_address="admin@amherst.co.uk",
#     )
#
#
# def packages_():
#     return [
#         ShipmentPackageRequest(
#             weight_in_grams=100,
#             package_format_identifier="smallParcel",
#         )
#     ]
#
#
# def order_():
#     return CreateOrderRequest(
#         recipient=recipient_(),
#         billing=billing_(),
#         order_date=datetime.datetime.now(),
#         subtotal=0,
#         shipping_cost_charged=0,
#         total=0,
#     )
#
#
# def orders_request():
#     return CreateOrdersRequest(
#         items=[order_()],
#     )
#
#
# def do_create_order():
#     req = orders_request()
#     with ApiClient(CONFIGURATION) as client:
#         c = OrdersApi(client)
#         try:
#             response = c.create_orders_async(create_orders_request=req)
#             pprint(response.model_dump(), indent=4, width=120)
#             return response
#
#         except ApiException as e:
#             print(e)
#             raise
#
#
# def do_cancel_order(o):
#     with ApiClient(CONFIGURATION) as rm:
#         client = OrdersApi(rm)
#         try:
#             response = client.delete_orders_async(order_identifiers=o)
#             pprint(response.model_dump(), indent=4, width=120)
#         except ApiException as e:
#             print(f"Exception when calling OrdersApi->delete_orders_async: {e}\n")
#             raise
#
#
# def do_list_orders():
#     with ApiClient(CONFIGURATION) as rm:
#         client = OrdersApi(rm)
#         try:
#             response = client.get_orders_async()
#             pprint(response.model_dump(), indent=4, width=120)
#             return response
#         except ApiException as e:
#             print(f"Exception when calling OrdersApi->delete_orders_async: {e}\n")
#             raise
#
#
# def do_get_label(order_idents: str, outpath):
#     with ApiClient(CONFIGURATION) as rm:
#         client = LabelsApi(rm)
#         try:
#             response: bytearray = client.get_orders_label_async(
#                 order_identifiers=order_idents,
#                 document_type="postageLabel",
#                 include_returns_label=False,
#                 include_cn=False,
#             )
#             with open(outpath, "wb") as f:
#                 f.write(response)
#         except ApiException as e:
#             print(f"Exception when calling LabelsApi->get_orders_label_async: {e}\n")
#             # raise
#         pprint(str(response), indent=4, width=120)
#
#
# def do_manifest():
#     with ApiClient(CONFIGURATION) as rm:
#         client = ManifestsApi(rm)
#         resp: ManifestOrdersResponse = client.manifest_eligible_async()
#         mainfest_num = resp.manifest_number
#         print(f"Manifest Number: {mainfest_num}")
#         return mainfest_num
#
#
# def test_main():
#     # HEALTHCHECK
#
#     # ADD AN ORDER TO THE SYSTEM
#     order_response: CreateOrdersResponse = do_create_order()
#     order_identifier = order_response.created_orders[0].order_identifier
#     # order_identifier = "1004"
#
#     # manifest orders
#     # res = do_manifest()
#
#     # GET LABELS
#     # save_to = f"RMCAD label_{order_identifier}.pdf"
#     # do_get_label(str(order_identifier), save_to)
#
#     #  TEARDOWN
#     res: GetOrdersResponse = do_list_orders()
#     order_ident_str = ";".join([str(_.order_identifier) for _ in res.orders])
#     do_cancel_order(order_ident_str)
