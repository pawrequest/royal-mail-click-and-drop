from datetime import date, datetime, timedelta

import pytest

from royal_mail_click_and_drop.models import CreateOrderRequest
from royal_mail_click_and_drop.models.shipment_package_request import PackageFormat

from royal_mail_click_and_drop.config import RoyalMailSettings

from royal_mail_click_and_drop import (
    AddressRequest,
    PostageDetailsRequest,
    RecipientDetailsRequest,
    ShipmentPackageRequest,
    CreateOrdersRequest,
    BillingDetailsRequest,
)
from royal_mail_click_and_drop.v2.consts import SendNotifcationsTo
from royal_mail_click_and_drop.v2.services import RoyalMailServiceCode


def no_weekends(d: date) -> date:
    if d.weekday() in (5, 6):
        d += timedelta(days=3)
    return d


def make_test_date(d: date) -> datetime:
    _test_date = no_weekends(d)
    return datetime.combine(_test_date, datetime.min.time())


TWO_DAYS_FUTURE = make_test_date(date.today() + timedelta(days=2))
TODAY = make_test_date(date.today())


@pytest.fixture(
    scope='session',
    params=[
        TODAY,
        # TWO_DAYS_FUTURE,
    ],
)
def sample_shipping_dates(request) -> datetime:
    return request.param


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
            weight_in_grams=10000,
            package_format_identifier=PackageFormat.PARCEL,
        )
        for _ in range(2)
    ]


@pytest.fixture(scope='session')
def sample_postage_details() -> PostageDetailsRequest:
    return PostageDetailsRequest(
        send_notifications_to=SendNotifcationsTo.RECIPIENT,
        service_code=RoyalMailServiceCode.EXPRESS_24,
        receive_email_notification=True,
        receive_sms_notification=True,
        # is_local_collect=True,
    )


@pytest.fixture(scope='session')
def _sample_order(recipient, sample_packages, sample_billing, sample_postage_details, sample_shipping_dates):
    return CreateOrderRequest(
        recipient=recipient.model_dump(),
        order_date=datetime.now(),
        subtotal=0,
        shipping_cost_charged=0,
        total=0,
        packages=sample_packages,
        billing=sample_billing,  # should be unnecessary with webportal settings
        postage_details=sample_postage_details,
        planned_despatch_date=sample_shipping_dates,
    )


@pytest.fixture(scope='session')
def sample_orders(_sample_order):
    return CreateOrdersRequest(
        items=[_sample_order],
    )


