"""
spotilyzer test mocks paginators base class
"""

# system imports
import os


class MockPaginatorsBase:

    def __init__(self):
        self.data_dir = os.path.join(os.path.dirname(__file__), 'data')
