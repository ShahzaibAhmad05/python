from abc import abstractmethod
from enum import Enum
from exceptions import BadOperatorException


class Operator:
    @abstractmethod
    def operate(self, num1: int | float, num2: int | float) -> int | float:
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        pass


class Add(Operator):
    def operate(self, num1: int | float, num2: int | float) -> int | float:
        return num1 + num2
    
    def __str__(self):
        return "Add"


class Subtract(Operator):
    def operate(self, num1: int | float, num2: int | float) -> int | float:
        return num1 - num2
    
    def __str__(self):
        return "Subtract"


class Divide(Operator):
    def operate(self, num1: int | float, num2: int | float) -> int | float:
        return num1 / num2
    
    def __str__(self):
        return "Divide"


class Multiply(Operator):
    def operate(self, num1: int | float, num2: int | float) -> int | float:
        return num1 * num2
    
    def __str__(self):
        return "Multiply"
    

def decode_operation(operator: str) -> Operator:
    """
    Decoding the operator class type and returning a usable instance
    
    Args:
        operator: the operator input given by the user
    
    Returns:
        usable instance of the operator type decoded

    Raises:
        BadOperatorException: in case of unknown operator or bad input
    """
    
    if operator == "+":
        return Add()
    elif operator == "-":
        return Subtract()
    elif operator == "/":
        return Divide()
    elif operator == "*":
        return Multiply()
    else:
        raise BadOperatorException("Unknown operator, bad input.")
    
