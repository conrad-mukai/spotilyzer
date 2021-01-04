"""
spotilyzer test mock boto3 client
"""

# system imports
import os
import json

# test imports
from .paginators import paginators

# constants
_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
_REGIONS_FILE = 'regions.json'
_AVAILABILITY_ZONES_FILE = 'availability-zones.json'


class MockBoto3Client:

    class Meta:
        region_name = 'us-west-2'

    meta = Meta()

    @staticmethod
    def describe_regions():
        with open(os.path.join(_DATA_DIR, _REGIONS_FILE)) as f:
            return json.load(f)

    @staticmethod
    def describe_availability_zones():
        with open(os.path.join(_DATA_DIR, _AVAILABILITY_ZONES_FILE)) as f:
            return json.load(f)

    @staticmethod
    def get_paginator(method):
        return paginators[method]
