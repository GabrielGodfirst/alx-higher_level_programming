#!/usr/bin/python3

"""Defines a rectangle class"""

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
        """
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
        """
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
        """
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
        """
        self.__y = value
