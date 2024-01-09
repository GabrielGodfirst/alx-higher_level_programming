class MyList(list):
    """
    A custom class MyList that inherits from the built-in list class.

    Public instance method:
    - print_sorted(self): Prints the list in ascending sorted order.

    Note: Assumes that all elements of the list are of type int.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        Parameters: None

        Returns: None
        """
        sorted_list = sorted(self)
        print(sorted_list)
