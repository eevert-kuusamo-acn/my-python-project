"""
Calculator module providing basic mathematical operations.

This module contains utility functions for basic arithmetic operations
and a Calculator class for performing calculations with operation strings.

Functions:
    add(a, b): Add two numbers together
    subtract(a, b): Subtract the second number from the first
    multiply(a, b): Multiply two numbers together

Classes:
    Calculator: A calculator class that performs operations based on string commands

Example:
    Basic usage of the calculator functions:
    
    >>> from calculator import add, subtract, multiply
    >>> add(2, 3)
    5
    >>> subtract(10, 4)
    6
    >>> multiply(3, 7)
    21
    
    Using the Calculator class:
    
    >>> calc = Calculator()
    >>> calc.calculate("add", 5, 3)
    8
"""


def add(a, b):
    """
    Add two numbers together.
    
    Performs basic addition of two numeric values.
    
    Args:
        a (float): The first number to add
        b (float): The second number to add
        
    Returns:
        float: The sum of a and b
        
    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(2.5, 1.5)
        4.0
    """
    return a + b


def subtract(a, b):
    """
    Subtract the second number from the first.
    
    Performs basic subtraction where the second argument is subtracted
    from the first argument.
    
    Args:
        a (float): The number to subtract from (minuend)
        b (float): The number to subtract (subtrahend)
        
    Returns:
        float: The difference of a and b (a - b)
        
    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(0, 5)
        -5
        >>> subtract(10.5, 2.5)
        8.0
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers together.
    
    Performs basic multiplication of two numeric values.
    
    Args:
        a (float): The first number to multiply
        b (float): The second number to multiply
        
    Returns:
        float: The product of a and b
        
    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(-2, 3)
        -6
        >>> multiply(2.5, 4)
        10.0
    """
    return a * b


class Calculator:
    """
    A simple calculator class for performing basic arithmetic operations.
    
    This class provides a way to perform calculations using string-based
    operation commands. It maintains an internal result state that can be
    used for tracking calculations.
    
    Attributes:
        result (float): The current result value, initialized to 0
        
    Supported Operations:
        - "add": Addition of two numbers
        - "subtract": Subtraction of two numbers
        
    Example:
        >>> calc = Calculator()
        >>> calc.calculate("add", 10, 5)
        15
        >>> calc.calculate("subtract", 20, 8)
        12
        >>> calc.calculate("invalid", 1, 2)  # Unsupported operation
        0
    """
    
    def __init__(self):
        """
        Initialize a new Calculator instance.
        
        Creates a calculator with an initial result value of 0.
        The result attribute can be used to track calculation state,
        though it is not automatically updated by the calculate method.
        """
        self.result = 0
    
    def calculate(self, operation, a, b):
        """
        Perform a calculation based on the specified operation string.
        
        This method accepts an operation string and two operands, then
        performs the corresponding calculation. If the operation is not
        supported, it returns 0.
        
        Args:
            operation (str): The operation to perform. Valid values are:
                - "add": Performs addition (a + b)
                - "subtract": Performs subtraction (a - b)
            a (float): The first operand
            b (float): The second operand
            
        Returns:
            float: The result of the calculation, or 0 if operation is unsupported
            
        Note:
            This method does not update the instance's result attribute.
            The result must be manually stored if needed.
            
        Examples:
            >>> calc = Calculator()
            >>> calc.calculate("add", 5, 3)
            8
            >>> calc.calculate("subtract", 10, 4)
            6
            >>> calc.calculate("multiply", 2, 3)  # Not supported
            0
        """
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        return 0