#!/usr/bin/python3

import json


class Base:
    """
    Base class for managing id attribute in future classes.
    """

    __nb_objects = 0

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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a file in JSON format.

        Args:
            list_objs (list): List of instances.

        Note:
            The filename is determined based on the class name.
        """
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string([obj.to_dictionary()
                                           for obj in list_objs]))

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a file.

        Returns:
            list: List of instances.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                data = file.read()
                dictionaries = cls.from_json_string(data)
                instances = [cls.create(**dictionary)
                             for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of dictionaries represented by the JSON string.

        Args:
            json_string (str): JSON string.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            cls: Instance of the class with attributes set.
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)  # Dummy instance
        elif cls.__name__ == "Square":
            instance = cls(1)  # Dummy instance
        instance.update(**dictionary)
        return instance
