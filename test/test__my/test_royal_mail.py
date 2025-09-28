"""
Integration tests for Royal Mail Click and Drop API

WARNING!!! RM DO NOT HAVE SANDBOX MODE THIS IS LIVE ACCOUNT!!!!

"""

import pytest

from royal_mail_click_and_drop import DeleteOrdersResource
from royal_mail_click_and_drop.config import royal_mail_settings
from royal_mail_click_and_drop.configuration import Configuration
from royal_mail_click_and_drop.models.create_orders_response import CreateOrdersResponse
from royal_mail_click_and_drop.models.get_orders_response import GetOrdersResponse
from royal_mail_click_and_drop.v2.actions import book_shipment, cancel_shipment, fetch_orders


@pytest.fixture
def config() -> Configuration:
    return royal_mail_settings().config


def test_lots(client, tmp_path, orders):
    # ADD AN ORDER TO THE SYSTEM
    order_response: CreateOrdersResponse = client.book_shipment(orders)
    order_identifier = order_response.created_orders[0].order_identifier
    assert order_identifier

    # manifest orders
    # res = do_manifest(config)

    # GET LABELS
    # save_to = tmp_path / f'RMCAD label_{order_identifier}.pdf'
    # do_get_label(str(order_identifier), save_to, config)

    #  TEARDOWN
    client.cancel_all_orders(really=True)



