"""
Integration tests for Royal Mail Click and Drop API

WARNING!!! RM DO NOT HAVE SANDBOX MODE THIS IS LIVE ACCOUNT!!!!

"""

import pytest

from royal_mail_click_and_drop.config import royal_mail_settings
from royal_mail_click_and_drop.configuration import Configuration
from royal_mail_click_and_drop.models.create_orders_response import CreateOrdersResponse


@pytest.fixture
def config() -> Configuration:
    return royal_mail_settings().config


def test_lots(client, tmp_path, orders):
    # ADD AN ORDER TO THE SYSTEM
    orders_og = client.fetch_orders()
    try:
        order_response: CreateOrdersResponse = client.book_shipment(orders)
        order_identifier = order_response.created_orders[0].order_identifier
        assert order_identifier
    finally:
        orders_after = client.fetch_orders()
        if orders_after != orders_og:
            for o in orders_after.orders:
                if o not in orders_og.orders:
                    res = client.cancel_shipment(order_ident=o.order_identifier)
                    assert o.order_identifier in [_.order_identifier for _ in res.deleted_orders]

    # manifest orders
    # res = do_manifest(config)

    # GET LABELS
    # save_to = tmp_path / f'RMCAD label_{order_identifier}.pdf'
    # do_get_label(str(order_identifier), save_to, config)


# def test_cancel_all(client):
#     client.cancel_all_orders()