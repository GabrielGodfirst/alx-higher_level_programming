#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8)
    and returns the number of characters written.

    Parameters:
    - filename (str): The name of the text file to write to
    (default is an empty string).
    - text (str): The string to be written to the file
    (default is an empty string).

    Returns:
    - int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        characters_written = file.write(text)
    return characters_written
