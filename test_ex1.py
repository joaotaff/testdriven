import pytest
import sys
import ex1

ex1_ = sys.modules['ex1']

def test_0():
    birth = "01/01/1990"
    ref = "01/01/2026"
    assert ex1_.ex1(birth, ref) == 36

def test_1():
    birth = "01/01/1990"
    ref = "31/12/2025"
    assert ex1_.ex1(birth, ref) == 35