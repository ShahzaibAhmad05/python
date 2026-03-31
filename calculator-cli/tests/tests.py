import pytest

# all the functions that have to be tested
from operation import (
    Add, Subtract, 
    Multiply, Divide, 
    decode_operation
)

# exception types to be used
from exceptions import (
    BadOperatorException
)


def test_add_operation():
    operation = Add()
    
    assert operation.operate(1, 6) == 7
    assert operation.operate(-1, -7) == -8
    assert operation.operate(0.3, 0.7) == 1.0


def test_subtract_operation():
    operation = Subtract()

    assert operation.operate(10, 4) == 6
    assert operation.operate(-5, -3) == -2
    assert operation.operate(0.5, 0.2) == 0.3


def test_multiply_operation():
    operation = Multiply()

    assert operation.operate(3, 4) == 12
    assert operation.operate(-2, 5) == -10
    assert operation.operate(0.5, 0.4) == 0.2


def test_divide_operation():
    operation = Divide()

    assert operation.operate(8, 2) == 4
    assert operation.operate(-9, 3) == -3
    assert operation.operate(0.6, 0.2) == 3


def test_decode_operation():
    assert isinstance(decode_operation("+"), Add)
    assert isinstance(decode_operation("-"), Subtract)
    assert isinstance(decode_operation("*"), Multiply)
    assert isinstance(decode_operation("/"), Divide)

    with pytest.raises(BadOperatorException):
        decode_operation("?")

