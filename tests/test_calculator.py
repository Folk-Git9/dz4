import pytest
from calculator import calc

def test_addition():
    assert calc.addition(2, 3) == 5
    assert calc.addition(-1, 1) == 0

def test_subtraction():
    assert calc.subtraction(5, 3) == 2
    assert calc.subtraction(0, 5) == -5

def test_multiplication():
    assert calc.multiplication(4, 3) == 12
    assert calc.multiplication(-2, 3) == -6

def test_division():
    assert calc.division(10, 2) == 5
    with pytest.raises(ValueError):
        calc.division(5, 0)

def test_exponentiation():
    assert calc.exponentiation(2, 3) == 8
    assert calc.exponentiation(5, 0) == 1

def test_square_root():
    assert calc.square_root(9) == 3
    with pytest.raises(ValueError):
        calc.square_root(-4)
