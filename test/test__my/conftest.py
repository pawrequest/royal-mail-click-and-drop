from datetime import datetime
from pprint import pprint
from collections.abc import Generator

import pytest

from royal_mail_click_and_drop.models import CreateOrderRequest
from royal_mail_click_and_drop.models.shipment_package_request import PackageFormat
from royal_mail_click_and_drop.v2.client import RoyalMailClient

from royal_mail_click_and_drop.config import RoyalMailSettings

from royal_mail_click_and_drop import (
    AddressRequest,
    PostageDetailsRequest,
    RecipientDetailsRequest,
    ShipmentPackageRequest,
    CreateOrdersRequest,
    BillingDetailsRequest,
    GetOrdersResponse,
)
from royal_mail_click_and_drop.v2.consts import SendNotifcationsTo
from royal_mail_click_and_drop.v2.services import RoyalMailServiceCode


# @pytest.fixture
# def config() -> Configuration:
#     return CONFIGURATION


@pytest.fixture(scope='session')
def sample_settings():
    return RoyalMailSettings.from_env('ROYAL_MAIL_ENV')


@pytest.fixture(scope='session')
def recip_address():
    return AddressRequest(
        full_name='Testy Testson',
        company_name='Comp name',
        address_line1='addr line1',
        address_line2='',
        address_line3='',
        city='city',
        county='county',
        postcode='da163hu',
        country_code='GB',
    )


@pytest.fixture(scope='session')
def sender_address():
    return AddressRequest(
        full_name='MY SENDER NAME',
        company_name='MY COMPANY NAME',
        address_line1='MY FIRSTLINE',
        address_line2='',
        address_line3='',
        city='MY CITY',
        county='COUNTY',
        postcode='me88sp',
        country_code='GB',
    )


@pytest.fixture(scope='session')
def recipient(recip_address):
    return RecipientDetailsRequest(
        address=recip_address,
        phone_number='07666666666',
        email_address='recipient@sdgikhjbsdgijbsdigj.com',
    )


@pytest.fixture(scope='session')
def sample_billing(sender_address):
    return BillingDetailsRequest(
        address=sender_address,
        phone_number='07888888888',
        email_address='billme@sikdjfsdjbfgjksbdgf.com',
    )


@pytest.fixture(scope='session')
def sample_packages():
    return [
        ShipmentPackageRequest(
            weight_in_grams=100,
            package_format_identifier=PackageFormat.PARCEL,
        )
    ]


#
@pytest.fixture(scope='session')
def sample_postage_details() -> PostageDetailsRequest:
    return PostageDetailsRequest(
        send_notifications_to=SendNotifcationsTo.BILLING,
        service_code=RoyalMailServiceCode.NEXT_DAY,
        receive_email_notification=True,
        receive_sms_notification=True,
    )


@pytest.fixture(scope='session')
def _sample_order(recipient, sample_packages, sample_billing, sample_postage_details):
    return CreateOrderRequest(
        recipient=recipient.model_dump(),
        order_date=datetime.now(),
        subtotal=0,
        shipping_cost_charged=0,
        total=0,
        packages=sample_packages,
        billing=sample_billing,  # should be unnecessary with webportal settings
        postage_details=sample_postage_details,
    )


@pytest.fixture(scope='session')
def sample_orders(_sample_order):
    return CreateOrdersRequest(
        items=[_sample_order],
    )


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
            assert o.order_identifier in [_.order_identifier for _ in res.deleted_orders], (
                'WARNING, FAILED TO DELETE TEST ORDERS!!'
            )
            print('Deleted Test Orders')
