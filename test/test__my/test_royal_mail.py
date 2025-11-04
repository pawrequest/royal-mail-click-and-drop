"""
Integration tests for Royal Mail Click and Drop API

WARNING!!! RM DO NOT HAVE SANDBOX MODE THIS IS LIVE ACCOUNT!!!!

sample_client should delete test orders but best to check [online portal](http://www.royalmail.com/oba)!

"""

from pprint import pprint
from collections.abc import Generator
from time import sleep

import pytest

from royal_mail_click_and_drop import GetOrdersResponse
from royal_mail_click_and_drop.exceptions import BadRequestException
from royal_mail_click_and_drop.models.create_orders_response import CreateOrdersResponse
from royal_mail_click_and_drop.v2.client import RoyalMailClient
import base64


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


def test_get_label(sample_client, sample_booking_response, tmp_path):
    idents = sample_booking_response.created_orders_idents_str
    label_data: bytearray = sample_client.get_save_label(idents, tmp_path / 'labels.pdf')
    print(f'\nLabel saved to {tmp_path / "labels.pdf"}')
    assert len(label_data) > 0


def test_created_order_ident_str(sample_booking_response):
    order_identifier = sample_booking_response.created_orders[0].order_identifier
    assert order_identifier == sample_booking_response.created_orders_idents[0]
    assert str(order_identifier) == sample_booking_response.created_orders_idents_str


def test_book_label_manifest(sample_client, tmp_path, sample_booking_response):
    orders = sample_client.fetch_orders()
    print('\nFetched Orders:')
    pprint(orders.model_dump(), indent=4, width=120)

    sleep(3)  # give api a moment to settle
    for i in range(1):
        try:
            res = sample_client.do_manifest()
            break
        except BadRequestException as e:
            print(f'Attempt {i + 1} to create manifest failed: {e}')
            sleep(3)
    else:
        raise RuntimeError('Failed to create manifest after several attempts')
    assert res.manifest_number is not None
    data64 = res.document_pdf
    data = data64.encode('utf-8')

    with open(tmp_path / 'manifest.pdf', 'wb') as f:
        f.write(base64.b64decode(data))
    print(f'Manifest saved to {tmp_path / "manifest.pdf"}')
    assert (tmp_path / 'manifest.pdf').stat().st_size > 0



