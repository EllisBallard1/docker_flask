"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_add_method():
    """Testing the Calculator Addition"""
    # Since the methods are now static, no longer need calculator = Calculator since we dont have to instantiate them multiple times

    assert Calculator.add(1, 1) == 2


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""

    assert Calculator.subtract(1, 1) == 0


def test_calculator_multiply_method():
    """Testing the Calculator Multiply"""

    assert Calculator.multiply(1, 1) == 1
