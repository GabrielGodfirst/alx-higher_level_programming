#!/usr/bin/python3

import csv
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor for Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the rectangle's position.
            y (int, optional): Y-coordinate of the rectangle's position.
            id (int, optional): Identifier for the rectangle.
            If None, the base class logic is used.

        Note:
            The super() call is used to invoke
            the constructor of the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        self.validate_non_negative_integer(value, 'width')
        if value <= 0:
            raise ValueError("[ValueError] width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        self.validate_non_negative_integer(value, 'height')
        if value <= 0:
            raise ValueError("[ValueError] height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        self.validate_non_negative_integer(value, 'x')
        if value < 0:
            raise ValueError("[ValueError] x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        self.validate_non_negative_integer(value, 'y')
        if value < 0:
            raise ValueError("[ValueError] y must be >= 0")
        self.__y = value

    def validate_non_negative_integer(self, value, attribute_name):
        """Validate that the input is a non-negative integer."""
        self.validate_integer(value, attribute_name)
        self.validate_non_negative(value, attribute_name)

    def validate_integer(self, value, attribute_name):
        """Validate that the input is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"[TypeError] {attribute_name} must be an integer")

    def validate_non_negative(self, value, attribute_name):
        """Validate that the input is greater than or equal to 0."""
        if value < 0:
            raise ValueError(f"[ValueError] {attribute_name} must be >= 0")

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance using '#' character."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Override the __str__ method to return the string representation."""
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """Assign attributes to the Rectangle instance."""
        if args:
            attr_list = ["id", "width", "height", "x", "y"]
            for attr, val in zip(attr_list, args):
                setattr(self, attr, val)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }

    def to_csv(self):
        """
        Return the CSV representation of the instance.

        Returns:
            list: List of values for CSV.
        """
        return [self.id, self.__width, self.__height, self.__x, self.__y]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of instances to a file in CSV format.
        Args:
        list_objs (list): List of instances.
        Note:
        The filename is determined based on the class name.

        """
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_csv())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load instances from a CSV file.
        Returns:
        list: List of instances.

        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    id, width, height, x, y = map(int, row)
                    instance = cls.create(id=id, width=width,
                                          height=height, x=x, y=y)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, *args, **kwargs):
        """
        Create an instance with all attributes already set.
        **kwargs can be thought of as a double pointer to a dictionary.
        To use the update method to assign all attributes, you must create a
        “dummy” instance before:
        """
        instance = cls(1, 1)
        instance.update(*args, **kwargs)
        return instance
