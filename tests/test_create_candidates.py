"""
spotilyzer create-candidates unit tests
"""

# system imports
import os
import json
import pathlib
from unittest.mock import MagicMock

# project imports
from spotilyzer import main

# test imports
from .test_base import BaseTestCase


class CreateCandidatesTestCase(BaseTestCase):

    def setUp(self):
        self.home = pathlib.Path.home

    def tearDown(self):
        pathlib.Path.home = self.home

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

    def test_user_seeds(self):
        pathlib.Path.home = MagicMock(return_value=self.data_dir)
        output = os.path.join(self.results_dir, 'nominal.json')
        self.assertEqual(main([
            'spotilyzer', 'create-candidates',
            '-d', '30',
            output
        ]), 0)
        with open(os.path.join(self.expected_dir, 'nominal.json')) as f:
            expected = json.load(f)
        with open(output) as f:
            results = json.load(f)
        self.assertEqual(expected, results)

    def test_package_seeds(self):
        pathlib.Path.home = MagicMock(return_value=self.results_dir)
        self.assertEqual(main([
            'spotilyzer', 'create-candidates',
            os.path.join(self.results_dir, 'package-seeds.json')
        ]), 0)

    def test_availability_zones(self):
        output = os.path.join(self.results_dir, 'nominal.json')
        self.assertEqual(main([
            'spotilyzer', 'create-candidates',
            '-a', 'us-west-2a,us-west-2b,us-west-2c,us-west-2d',
            '-d', '30',
            '-s', os.path.join(self.data_dir, 'seeds.json'),
            output
        ]), 0)
        with open(os.path.join(self.expected_dir, 'nominal.json')) as f:
            expected = json.load(f)
        with open(output) as f:
            results = json.load(f)
        self.assertEqual(expected, results)

    def test_region(self):
        output = os.path.join(self.results_dir, 'nominal.json')
        self.assertEqual(main([
            'spotilyzer', 'create-candidates',
            '-d', '30',
            '-s', os.path.join(self.data_dir, 'seeds.json'),
            '-r', 'us-east-1',
            output
        ]), 0)
        with open(os.path.join(self.expected_dir, 'nominal.json')) as f:
            expected = json.load(f)
        with open(output) as f:
            results = json.load(f)
        self.assertEqual(expected, results)

    def test_bad_duration(self):
        self.assertNotEqual(main([
            'spotilyzer', 'create-candidates',
            '-d', 'x',
            'none.json'
        ]), 0)
