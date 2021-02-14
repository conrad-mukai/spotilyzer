"""
spotilyzer show-candidates unit tests
"""

# system imports
import os
import sys

# project imports
from spotilyzer import main

# test imports
from .test_base import BaseTestCase


class ShowCandidatesTestCase(BaseTestCase):

    def test_nominal(self):
        output = os.path.join(self.results_dir, 'candidates-tabulate.txt')
        stdout = sys.stdout
        sys.stdout = open(output, 'w')
        try:
            self.assertEqual(main([
                'spotilyzer', 'show-candidates',
                os.path.join(self.expected_dir, 'nominal.json')
            ]), 0)
        finally:
            sys.stdout.close()
            sys.stdout = stdout
        with open(output) as f:
            results = f.read()
        with open(os.path.join(self.expected_dir,
                               'candidates-tabulate.txt')) as f:
            expected = f.read()
        self.assertEqual(expected, results)
