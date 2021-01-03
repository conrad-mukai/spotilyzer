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

class MockBoto3Client(object):

    class Meta(object):
        region_name = 'us-west-2'

    meta = Meta()

    def describe_regions(self):
        with open(os.path.join(_DATA_DIR, _REGIONS_FILE)) as f:
            return json.load(f)

    def describe_availability_zones(self):
        with open(os.path.join(_DATA_DIR, _AVAILABILITY_ZONES_FILE)) as f:
            return json.load(f)

    def get_paginator(self, method):
        return paginators[method]
