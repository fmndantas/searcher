import pytest
from searcher import *

# modules used in tests so far: numpy, matplotlib

import numpy, matplotlib

def test_search():
    subpackages, modules = search('array', numpy)