#!/usr/bin/python3

import json


class Base:
    """
    Base class for managing id attribute in future classes.
    """

    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """
        Class constructor for Base.

        Args:
            id (int, optional): If provided,
                assign it to the public instance attribute 'id'.
                Otherwise, increment __nb_objects and
                assign the new value to 'id'.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
