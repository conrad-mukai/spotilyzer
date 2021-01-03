"""
spotilyzer test mock describe_instance_type_offerings paginator
"""

# system imports
import os
import json

# test imports
from .base import MockPaginatorsBase

class MockDescribeInstanceTypeOfferingsPaginator(MockPaginatorsBase):

    def paginate(self, **kwargs):
        for filter in kwargs['Filters']:
            if filter['Name'] == 'instance-type':
                instance_type = filter['Values'][0]
                if instance_type.startswith('c'):
                    group = 'compute'
                elif instance_type.startswith('m'):
                    group = 'general'
                elif instance_type.startswith('r'):
                    group = 'memory'
                else:
                    raise RuntimeError("unexpected "
                                       "describe_instance_type_offerings "
                                       "input")
                break
        with open(os.path.join(self.data_dir, 'instance-type-offerings',
                               f"{group}.json")) as f:
            yield json.load(f)
