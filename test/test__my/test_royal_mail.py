"""
Integration tests for Royal Mail Click and Drop API

WARNING!!! RM DO NOT HAVE SANDBOX MODE THIS IS LIVE ACCOUNT!!!!

sample_client should delete test orders but best to check [online portal](http://www.royalmail.com/oba)!

"""

from pprint import pprint
from collections.abc import Generator

import pytest

from royal_mail_click_and_drop import GetOrdersResponse
from royal_mail_click_and_drop.models.create_orders_response import CreateOrdersResponse
from royal_mail_click_and_drop.v2.client import RoyalMailClient


@pytest.fixture(scope='session')
def sample_client(sample_settings) -> Generator[RoyalMailClient, None, None]:
    """Test client - automatically removes orders created during testing on completion"""
    client = RoyalMailClient(settings=sample_settings)
    orders_before: GetOrdersResponse = client.fetch_orders()
    pprint(orders_before.model_dump())

    yield client

    print('Deleting Test Orders')
    orders_after: GetOrdersResponse = client.fetch_orders()
    for o in orders_after.orders:
        if o not in orders_before.orders:
            res = client.cancel_shipment(order_ident=o.order_identifier)
            assert o.order_identifier in res.idents, 'WARNING, FAILED TO DELETE TEST ORDERS!!'
            print('Deleted Test Orders')


@pytest.fixture(scope='session')
def sample_booking_response(sample_client, sample_orders) -> CreateOrdersResponse:
    return sample_client.book_shipment(sample_orders)


def test_book_order(sample_booking_response):
    order_identifier = sample_booking_response.created_orders[0].order_identifier
    assert order_identifier


def test_created_order_ident_str(sample_booking_response):
    order_identifier = sample_booking_response.created_orders[0].order_identifier
    assert order_identifier == sample_booking_response.created_orders_idents[0]
    assert str(order_identifier) == sample_booking_response.created_orders_idents_str


# def test_get_label(sample_client, sample_booking_response, tmp_path):
# manifest orders
# res = do_manifest(config)

# GET LABELS
# save_to = tmp_path / f'RMCAD label_{order_identifier}.pdf'
# do_get_label(str(order_identifier), save_to, config)

