#!/usr/bin/python3

"""This module defines a function to add two integers.

This module contains a single function, add_integer, which takes two arguments
and returns their sum.

"""


def add_integer(a, b=98):

    """Add two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float,
        which by default is 98.

    Returns:
        int: The sum of a and b, casted to an integer.

    Raises:
        TypeError: If a or b is not an integer or float.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
    """

    # Check if a and b are integers or floats
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or float")

    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer or float")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the sum of a and b
    return int(a + b)
