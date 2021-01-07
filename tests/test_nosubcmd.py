"""
spotilyzer unit tests
"""

# project imports
from spotilyzer import main

# test imports
from .test_base import BaseTestCase


class NoSubcmdTestCase(BaseTestCase):

    def test_nominal(self):
        self.assertEqual(main([
            'spotilyzer', '-h'
        ]).code, 0)

    def test_fail(self):
        self.assertNotEqual(main([
            'spotilyzer'
        ]), 0)
