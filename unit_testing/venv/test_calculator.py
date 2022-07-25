import pytest
from calculator import Calculator, CalculatorError
def test_add():
    # Arrange
    # Act
    # Assert
    calculator = Calculator()
    result = calculator.add(3, 2)
    assert result == 5

def test_add_with_weird_input():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        calculator.add(3, 'a')

def test_subtract():
    calculator = Calculator()
    result = calculator.subtract(3, 2)
    assert result == 1

def test_multiply():
    calculator = Calculator()
    result = calculator.multiply(3, 2)
    assert result == 6
