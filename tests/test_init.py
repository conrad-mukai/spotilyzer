"""
spotilyzer init unit tests
"""

# system imports
import pathlib
from unittest.mock import MagicMock
import os
import json

# project imports
from spotilyzer import main
from spotilyzer.subcommands.utils.paths import SEEDS_FILE, _USER_DIR, \
    get_package_datadir

# test imports
from .test_base import BaseTestCase


class InitTestCase(BaseTestCase):

    def setUp(self):
        self.home = pathlib.Path.home
        pathlib.Path.home = MagicMock(return_value=self.results_dir)

    def tearDown(self):
        pathlib.Path.home = self.home

    def test_nominal(self):
        self.assertEqual(main([
            'spotilyzer', 'init'
        ]), 0)
        with open(os.path.join(self.results_dir, _USER_DIR, SEEDS_FILE)) as f:
            results = json.load(f)
        with open(os.path.join(get_package_datadir(), SEEDS_FILE)) as f:
            expected = json.load(f)
        self.assertEqual(expected, results)
