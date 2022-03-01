"""Testing the Operations"""
from calculator.operations import Operations


def test_calculator_add_method():
    """Testing addition method"""
    assert Operations.add(1, 1) == 2


def test_calculator_subtract_method():
    """Testing subtraction method"""
    assert Operations.subtract(1, 1) == 0


def test_calculator_multiply_method():
    """Testing multiply method"""
    assert Operations.multiply(1, 1) == 1
