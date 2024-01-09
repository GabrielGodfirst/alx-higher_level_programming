#!/usr/bin/python3

"""
This module provides a function that looks
up for the available attributes and objects of
an object.
"""


def lookup(obj):

    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    - obj: Any object to inspect.

    Returns:
    - List of strings representing attributes and methods of the object.
    """
    # Get the attributes and methods of the object
    obj_attributes = [attr for attr in dir(obj)
                      if not callable(getattr(obj, attr))
                      or callable(getattr(obj, attr))
                      and not attr.startswith("__")]

    return obj_attributes
