"""
spotilyzer test base class
"""

# system imports
import unittest
from unittest.mock import MagicMock
import datetime
import os
import shutil

# 3rd party imports
import boto3
import tabulate

# test imports
from .mocks.boto3_client import MockBoto3Client
from .mocks.datettime import MockDateTime
from .mocks.tabulate import mock_tabulate
from .paths import TEST_DIR, DATA_DIR, RESULTS_DIR, EXPECTED_DIR


class BaseTestCase(unittest.TestCase):

    test_dir = TEST_DIR
    data_dir = DATA_DIR
    results_dir = RESULTS_DIR
    expected_dir = EXPECTED_DIR

    @classmethod
    def setUpClass(cls):
        boto3.client = MagicMock(return_value=MockBoto3Client())
        datetime.datetime = MockDateTime
        tabulate.tabulate = mock_tabulate
        os.makedirs(cls.results_dir, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.results_dir)
