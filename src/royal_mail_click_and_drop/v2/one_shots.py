from functools import lru_cache

from royal_mail_click_and_drop.config import RoyalMailSettings
from royal_mail_click_and_drop.v2.client import RoyalMailClient


@lru_cache
def get_settings():
    return RoyalMailSettings.from_env('ROYAL_MAIL_ENV')


@lru_cache
def get_client():
    return RoyalMailClient(settings=get_settings())


def cancel_order(ident: str):
    client = get_client()
    res = client.cancel_shipment(ident)
    res_idents = res.deleted_order_idents
    print(res_idents)
