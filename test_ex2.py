import pytest
import sys
import ex2

ex2_ = sys.modules['ex2']


def test_0():
    strnum = ""
    assert ex2_.ex2(strnum) == 0

def test_1():
    strnum = 3
    with pytest.raises(TypeError, match="Input must be a string"):
        ex2_.ex2(strnum)