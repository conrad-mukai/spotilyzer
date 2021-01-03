"""
spotilyzer group-requests unit tests
"""

# system imports
import os
import json

# project imports
from spotilyzer import main

# test imports
from .test_base import BaseTestCase


class GroupRequestsTestCase(BaseTestCase):

    def test_nominal(self):
        output = os.path.join(self.results_dir, 'requests.json')
        self.assertEqual(main([
            'spotilyzer', 'group-requests',
            os.path.join(self.expected_dir, 'nominal.json'),
            os.path.join(self.data_dir, 'requests.csv'),
            output
        ]), 0)
        with open(os.path.join(self.expected_dir, 'requests.json')) as f:
            expected = json.load(f)
        with open(output) as f:
            results = json.load(f)
        self.assertEqual(expected, results)
