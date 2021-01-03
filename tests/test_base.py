"""
spotilyzer test base class
"""

# system imports
import unittest
from unittest.mock import MagicMock
import datetime
import sys
import os
import shutil

# 3rd party imports
import boto3
import tabulate

# test imports
from .mocks.boto3_client import MockBoto3Client
from .mocks.datettime import MockDateTime
from .mocks.tabulate import mock_tabulate

# constants
_TEST_DIR = os.path.dirname(__file__)
_DATA_DIR = 'data'
_RESULTS_DIR = 'results'
_EXPECTED_DIR = 'expected'

class BaseTestCase(unittest.TestCase):

    test_dir = _TEST_DIR
    data_dir = os.path.join(test_dir, _DATA_DIR)
    results_dir = os.path.join(test_dir, _RESULTS_DIR)
    expected_dir = os.path.join(test_dir, _EXPECTED_DIR)

    @classmethod
    def setUpClass(cls):
        boto3.client = MagicMock(return_value=MockBoto3Client())
        datetime.datetime = MockDateTime
        tabulate.tabulate = mock_tabulate
        os.makedirs(cls.results_dir, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.results_dir)

    def setUp(self):
        self.stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def tearDown(self):
        sys.stdout.close()
        sys.stdout = self.stdout
