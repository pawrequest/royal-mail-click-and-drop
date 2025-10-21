from enum import StrEnum


class RoyalMailServiceCode(StrEnum):
    NEXT_DAY = 'TOLP24'  # no signature... use 'TOLP24SF' for signature
    NEXT_DAY_12 = 'SD1OLP'  # £750 comp... use 'SD2OLP' for 1,000 or 'SD3OLP' for 2,500
