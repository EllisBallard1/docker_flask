"""Testing the Operations"""
from calculator.operations import Addition, Subtraction, Multiplication


def test_calculator_add_method():
    """Testing addition method"""
    assert Addition.add(1, 1) == 2


def test_calculator_subtract_method():
    """Testing subtraction method"""
    assert Subtraction.subtract(1, 1) == 0


def test_calculator_multiply_method():
    """Testing multiply method"""
    assert Multiplication.multiply(1, 1) == 1
