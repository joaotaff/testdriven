import pytest
import sys
import ex2

ex2_ = sys.modules['ex2']


def test_0():
    strnum = ""
    assert ex2_.ex2(strnum) == 0