""" This is the Calculator Class"""
from calculator.operations import Addition, Subtraction, Multiplication
"""we want to have a history of calculations, 3/3/22"""


class Calculator:
    """ This is the default result property"""
    result = 0

    """when the method becomes a static method, we no longer need self"""
    @staticmethod
    def add(value_1, value_2):
        """ This is the add method"""
        # Call the static method add to return the sum and set it to the calculator result
        return Addition.add(value_1, value_2)

    @staticmethod
    def subtract(value_1, value_2):
        """ This is the subtract method"""
        return Subtraction.subtract(value_1, value_2)

    @staticmethod
    def multiply(value_1, value_2):
        """ This is the subtract method"""
        return Multiplication.multiply(value_1, value_2)

    @staticmethod
    def get_result(self):
        """ This is the get result method"""
        return self.result
