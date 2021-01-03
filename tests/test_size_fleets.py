"""
spotilyzer size-fleets unit tests
"""

# system imports
import os
import json

# project imports
from spotilyzer import main

# test imports
from .test_base import BaseTestCase


class SizeFleetsTestCase(BaseTestCase):

    def test_nominal(self):
        self.assertEqual(main([
            'spotilyzer', 'size-fleets',
            os.path.join(self.expected_dir, 'nominal.json'),
            os.path.join(self.expected_dir, 'requests.json')
        ]), 0)
        with open(os.path.join(self.expected_dir,
                               'size-fleets-tabulate.txt')) as f:
            expected = f.read()
        with open(os.path.join(self.results_dir, 'tabulate.txt')) as f:
            results = f.read()
        self.assertEqual(expected, results)
