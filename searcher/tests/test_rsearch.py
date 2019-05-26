import pytest
from searcher.searcher import rsearch, get_pack_dir

# modules used in tests so far: numpy, matplotlib

import numpy, matplotlib

def test_rsearch():
    lib_path = get_pack_dir(numpy)
    path = rsearch('compat', lib_path)
    assert path is not None
    