# coding: utf-8

"""
    Go Sidecar Accelerator

    This is a sample API written to become a Sidecar leveraging the Gin Go framework.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: tristan.leonard1@ibm.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.storage_api import StorageApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStorageApi(unittest.TestCase):
    """StorageApi unit test stubs"""

    def setUp(self):
        self.api = StorageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_download_file(self):
        """Test case for download_file

        Download a file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()