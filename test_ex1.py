import pytest
import sys
import ex1

ex1_ = sys.modules['ex1']

def test_0():
    birth = "01/01/2000"
    ref = "01/01/2026"
    assert ex1_.ex1(birth, ref) == 26

def test_1():
    birth = "01/01/2000"
    ref = "31/12/2025"
    assert ex1_.ex1(birth, ref) == 25

def test_2():
    birth = "29/02/2000"
    ref = "01/03/2026"
    assert ex1_.ex1(birth, ref) == 26

def test_3():
    birth = "01/01/2000"
    ref = "01/01/1999"
    with pytest.raises(ValueError, match=r".* after reference date.*"):
        ex1_.ex1(birth, ref)

def test_4():
    birth = "apple"
    ref = "01/01/2026"
    with pytest.raises(ValueError, match=r"Invalid birthdate format"):
        ex1_.ex1(birth, ref)

def test_5():
    birth = "01/01/2000"
    ref = "apple"
    with pytest.raises(ValueError, match=r"Invalid reference date format"):
        ex1_.ex1(birth, ref)