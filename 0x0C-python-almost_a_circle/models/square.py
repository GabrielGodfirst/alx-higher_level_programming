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

    def __str__(self):
        """
        Override the __str__ method to return the string representation.

        Returns:
            str: Formatted string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
