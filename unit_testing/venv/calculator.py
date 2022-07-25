import numbers


class CalculatorError(Exception):
    """Exception raised when calculator errors occur."""
    pass

class Calculator:
    """A terrible calculator"""
    def add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        try:
            return a + b
        except TypeError:
            raise CalculatorError('Invalid input')

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError('Invalid input')

if __name__ == '__main__':
    print("lets calculate  ")
    c = Calculator()
    print(c.add(3, 2))