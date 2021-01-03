"""
spotilyzer tests mock tabulate function
"""

# system imports
import os

# 3rd party imports
import tabulate
from tabulate import tabulate as _tabulate

# constants
_RESULTS_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir,
                            'results')


def mock_tabulate(*args, **kwargs):
    display = _tabulate(*args, **kwargs)
    with open(os.path.join(_RESULTS_DIR, 'tabulate.txt'), 'w') as f:
        f.write(display)
    return display
