"""
spotilyzer test mock describe_spot_price_history paginator
"""

# system
import os
import pickle

# test imports
from .base import MockPaginatorsBase


class MockDescribeSpotPriceHistoryPaginator(MockPaginatorsBase):

    def paginate(self, **kwargs):
        spot_price_dir = os.path.join(self.data_dir, 'spot-price-history',
                                      kwargs['AvailabilityZone'])
        for fname in sorted(os.listdir(spot_price_dir)):
            with open(os.path.join(spot_price_dir, fname), 'rb') as f:
                yield pickle.load(f)
