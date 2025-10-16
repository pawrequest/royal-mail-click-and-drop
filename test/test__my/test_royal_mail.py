"""
Integration tests for Royal Mail Click and Drop API

WARNING!!! RM DO NOT HAVE SANDBOX MODE THIS IS LIVE ACCOUNT!!!!

sample_client should delete test orders but best to check [online portal](http://www.royalmail.com/oba)!

"""

from royal_mail_click_and_drop.models.create_orders_response import CreateOrdersResponse


def test_lots(sample_client, tmp_path, orders):
    order_response: CreateOrdersResponse = sample_client.book_shipment(orders)
    order_identifier = order_response.created_orders[0].order_identifier
    assert order_identifier

    # manifest orders
    # res = do_manifest(config)

    # GET LABELS
    # save_to = tmp_path / f'RMCAD label_{order_identifier}.pdf'
    # do_get_label(str(order_identifier), save_to, config)


# def test_cancel_all(client):
#     client.cancel_all_orders()
