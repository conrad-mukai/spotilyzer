"""
spotilyzer datetime mock class
"""

# system imports
import datetime

# constants
_TIMESTAMP = '2021-01-01T22:14:13.120426'
_ISO_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'


class MockDateTime(datetime.datetime):

    @classmethod
    def now(cls):
        return datetime.datetime.strptime(_TIMESTAMP, _ISO_FORMAT)
