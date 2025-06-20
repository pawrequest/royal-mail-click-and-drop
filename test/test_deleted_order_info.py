# coding: utf-8

"""
    ChannelShipper & Royal Mail Public API

    Import your orders, retrieve your orders and generate labels.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from royal_mail_click_and_drop.models.deleted_order_info import DeletedOrderInfo

class TestDeletedOrderInfo(unittest.TestCase):
    """DeletedOrderInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeletedOrderInfo:
        """Test DeletedOrderInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeletedOrderInfo`
        """
        model = DeletedOrderInfo()
        if include_optional:
            return DeletedOrderInfo(
                order_identifier = 56,
                order_reference = '',
                order_info = ''
            )
        else:
            return DeletedOrderInfo(
        )
        """

    def testDeletedOrderInfo(self):
        """Test DeletedOrderInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
