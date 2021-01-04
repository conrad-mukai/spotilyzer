"""
spotilyzer tests mock tabulate function
"""

# system imports
import os

# 3rd party imports
from tabulate import tabulate as _tabulate

# test imports
from ..paths import RESULTS_DIR


def mock_tabulate(*args, **kwargs):
    display = _tabulate(*args, **kwargs)
    with open(os.path.join(RESULTS_DIR, 'tabulate.txt'), 'w') as f:
        f.write(display)
    return display
