from enum import StrEnum


class RoyalMailServiceCodeClickDrop(StrEnum):
    TRACKED_24 = 'TOLP24'  # no signature.
    TRACKED_24_SIGNED = 'TOLP24SF'
    SPECIAL_PRE_12 = 'SD1OLP'  # £750 comp... use 'SD2OLP' for 1,000 or 'SD3OLP' for 2,500
    EXPRESS_24 = 'PFE24'
    EXPRESS_24_PRE_10 = 'PFE10'


class RoyalMailServiceCode(StrEnum):
    EXPRESS_24 = 'NDA'
    FIRST_CLASS_SIGNED = 'BPR1'
    EXPRESS_AM = 'FEE'
    EXPRESS_10 = 'TE1'
    SPECIAL_1PM = 'SD1'
    SPECIAL_9AM = 'SD4'


class RoyalMailServiceCodeFull(StrEnum):
    InternationalEconomy = 'IEOLP'
    InternationalSigned = 'ISIOLP'
    InternationalSignedDuplicate = 'ISIOLP'
    InternationalStandard = 'ISOLP'
    InternationalTrackedHeavier = 'ITHCOLP'
    InternationalTrackedHeavierDuplicate = 'ITHCOLP'
    InternationalTrackedSignedHeavier = 'ITHOLPSF'
    InternationalTrackedSignedHeavierDuplicate = 'ITHOLPSF'
    InternationalTracked = 'ITROLP'
    InternationalTrackedDuplicate = 'ITROLP'
    InternationalTrackedSigned = 'ITSOLP'
    InternationalTrackedSignedDuplicate = 'ITSOLP'
    RoyalMail1stClass = 'OLP1'
    RoyalMailSignedFor1stClass = 'OLP1SF'
    RoyalMail2ndClass = 'OLP2'
    RoyalMailSignedFor2ndClass = 'OLP2SF'
    express10 = 'PFE10'
    express10Comp1 = 'PFE10'
    express10Comp2 = 'PFE10'
