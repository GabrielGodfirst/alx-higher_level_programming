#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor for Square.

        Args:
            size (int): Size of the square (width and height).
            x (int, optional): X-coordinate of the square's position.
            y (int, optional): Y-coordinate of the square's position.
            id (int, optional): Identifier for the square.
            If None, the base class logic is used.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width  # Since size is the same as width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value

    def __str__(self):
        """Override the __str__ method to return the string representation."""
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}"
        )
