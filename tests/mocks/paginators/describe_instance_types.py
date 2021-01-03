"""
spotilyzer test mock describe_instance_types paginator
"""

# system imports
import os
import json

# test imports
from .base import MockPaginatorsBase


class MockDescribeInstanceTypesPaginator(MockPaginatorsBase):

    def __init__(self):
        super(MockDescribeInstanceTypesPaginator, self).__init__()
        self.group = None
        self.response = None
        self.response_map = None

    def paginate(self, **kwargs):
        instance_types_requested = kwargs['InstanceTypes']
        family = instance_types_requested[0][0]
        if family == 'c':
            group = 'compute'
        elif family == 'm':
            group = 'general'
        elif family == 'r':
            group = 'memory'
        else:
            raise RuntimeError("unrecognized instance type")
        if self.group != group:
            self.group = group
            with open(os.path.join(self.data_dir, 'instance-types',
                                   f'{self.group}.json')) as f:
                self.response = json.load(f)
            instance_types = self.response['InstanceTypes']
            self.response_map = {
                instance_types[i]['InstanceType']: i
                for i in range(len(instance_types))
            }
        instance_types_response = self.response['InstanceTypes']
        yield {
            'InstanceTypes': [
                instance_types_response[self.response_map[i]]
                for i in instance_types_requested
            ]
        }
