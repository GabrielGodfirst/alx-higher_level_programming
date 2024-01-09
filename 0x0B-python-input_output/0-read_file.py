def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout.

    Parameters:
    - filename (str): The name of the text file to read
      (default is an empty string).

    Returns:
    - None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)


if __name__ == "__main__":

    file_name = "my_file_0.txt"
    read_file(file_name)
