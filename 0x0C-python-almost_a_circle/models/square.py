#!/usr/bin/python3

"""Defines the Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor for Square.

        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate of the square's position.
            y (int, optional): Y-coordinate of the square's position.
            id (int, optional): Identifier for the square. If None,
            the base class logic is used.

        Note:
            The super() call is used to invoke
            the constructor of the Rectangle class.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: Size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): New size value.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If size is <= 0.
        """
        self.validate_non_negative_integer(value, 'width')
        self.width = value
        self.height = value

    def __str__(self):
        """
        Override the __str__ method to return the string representation.

        Returns:
            str: Formatted string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
