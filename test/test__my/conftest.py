import os
from datetime import datetime

import pytest
os.environ['ROYAL_MAIL_ENV'] = r'C:\prdev\envs\sandbox\royal_mail.env'

from royal_mail_click_and_drop.models import CreateOrderRequest
from royal_mail_click_and_drop.v2.client import RoyalMailClient

from royal_mail_click_and_drop.config import royal_mail_settings

SETTINGS = royal_mail_settings()
from royal_mail_click_and_drop import (
    Configuration,
    AddressRequest,
    RecipientDetailsRequest,
    ShipmentPackageRequest,
    CreateOrdersRequest,
    BillingDetailsRequest,
)

CONFIGURATION = Configuration(host=SETTINGS.base_url, api_key={'Bearer': SETTINGS.api_key})


@pytest.fixture
def config() -> Configuration:
    return CONFIGURATION


@pytest.fixture
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


@pytest.fixture()
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


@pytest.fixture
def recipient(recip_address):
    return RecipientDetailsRequest(
        address=recip_address,
        phone_number='07666666666',
        email_address='recipient@sdgikhjbsdgijbsdigj.com',
    )


@pytest.fixture
def billing_(sender_address):
    return BillingDetailsRequest(
        address=sender_address,
        phone_number='07888888888',
        email_address='billme@sikdjfsdjbfgjksbdgf.com',
    )


@pytest.fixture
def packages_():
    return [
        ShipmentPackageRequest(
            weight_in_grams=100,
            package_format_identifier='smallParcel',
        )
    ]


@pytest.fixture
def order(recipient, packages_, billing_):
    return CreateOrderRequest(
        recipient=recipient.model_dump(),
        order_date=datetime.now(),
        subtotal=0,
        shipping_cost_charged=0,
        total=0,
        packages=packages_,
        billing=billing_,
    )


@pytest.fixture
def orders(order):
    return CreateOrdersRequest(
        items=[order],
    )

@pytest.fixture
def client() -> RoyalMailClient:
    return RoyalMailClient()