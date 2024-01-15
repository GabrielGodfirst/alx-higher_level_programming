#!/usr/bin/python3

"""Defines the rectangle class and its function"""

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
            id (int, optional): Identifier for the rectangle. If None,
            the base class logic is used.

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
        """
        Getter for the width attribute.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If width is <= 0.
        """
        self.validate_non_negative_integer(value, 'width')
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If height is <= 0.
        """
        self.validate_non_negative_integer(value, 'height')
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
            int: X-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Args:
            value (int): New x-coordinate value.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If x is < 0.
        """
        self.validate_non_negative(value, 'x')
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
            int: Y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Args:
            value (int): New y-coordinate value.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If y is < 0.
        """
        self.validate_non_negative(value, 'y')
        self.__y = value

    def validate_non_negative_integer(self, value, attribute_name):
        """
        Validate that the input is a non-negative integer.

        Args:
            value: Input value to be validated.
            attribute_name (str): Name of the attribute for error message.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the input is not a non-negative integer.
        """
        self.validate_integer(value, attribute_name)
        self.validate_non_negative(value, attribute_name)

    def validate_integer(self, value, attribute_name):
        """
        Validate that the input is an integer.

        Args:
            value: Input value to be validated.
            attribute_name (str): Name of the attribute for error message.

        Raises:
            TypeError: If the input is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")

    def validate_non_negative(self, value, attribute_name):
        """
        Validate that the input is greater than or equal to 0.

        Args:
            value: Input value to be validated.
            attribute_name (str): Name of the attribute for error message.

        Raises:
            ValueError: If the input is < 0.
        """
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Print the Rectangle instance using '#' character.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Override the __str__ method to return the string representation.

        Returns:
            str: Formatted string representation of the Rectangle instance.
        """
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle.

        Args:
            *args: Arguments to update the attributes in the order:
                   1st argument: id attribute
                   2nd argument: width attribute
                   3rd argument: height attribute
                   4th argument: x attribute
                   5th argument: y attribute
            **kwargs: Key-value pairs to update the attributes.
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
