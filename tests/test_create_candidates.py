"""
spotilyzer create-candidates unit tests
"""

# system imports
import os
import json

# project imports
from spotilyzer import main

# test imports
from .test_base import BaseTestCase


class CreateCandidatesTestCase(BaseTestCase):

    def test_nominal(self):
        output = os.path.join(self.results_dir, 'nominal.json')
        self.assertEqual(main([
            'spotilyzer', 'create-candidates',
            '-d', '30',
            '-s', os.path.join(self.data_dir, 'seeds.json'),
            output
        ]), 0)
        with open(os.path.join(self.expected_dir, 'nominal.json')) as f:
            expected = json.load(f)
        with open(output) as f:
            results = json.load(f)
        self.assertEqual(expected, results)
