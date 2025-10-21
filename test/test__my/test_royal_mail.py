"""
Integration tests for Royal Mail Click and Drop API

WARNING!!! RM DO NOT HAVE SANDBOX MODE THIS IS LIVE ACCOUNT!!!!

sample_client should delete test orders but best to check [online portal](http://www.royalmail.com/oba)!

"""

import pytest

from royal_mail_click_and_drop.models.create_orders_response import CreateOrdersResponse


@pytest.fixture(scope='session')
def sample_booking_response(sample_client, sample_orders) -> CreateOrdersResponse:
    return sample_client.book_shipment(sample_orders)


def test_lots(sample_booking_response, tmp_path):
    order_identifier = sample_booking_response.created_orders[0].order_identifier
    order_ident2 = sample_booking_response.created_orders_idents
    assert order_identifier
    assert order_ident2 == str(order_identifier)

    # manifest orders
    # res = do_manifest(config)

    # GET LABELS
    # save_to = tmp_path / f'RMCAD label_{order_identifier}.pdf'
    # do_get_label(str(order_identifier), save_to, config)


# def test_cancel_all(client):
#     client.cancel_all_orders()
