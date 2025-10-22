from enum import StrEnum


class RoyalMailServiceCode(StrEnum):
    TRACKED_24 = 'TOLP24'  # no signature.
    TRACKED_24_SIGNED = 'TOLP24SF'
    SPECIAL_PRE_12 = 'SD1OLP'  # £750 comp... use 'SD2OLP' for 1,000 or 'SD3OLP' for 2,500
    EXPRESS_24 = 'PFE24'
    EXPRESS_24_PRE_10 = 'PFE10'


