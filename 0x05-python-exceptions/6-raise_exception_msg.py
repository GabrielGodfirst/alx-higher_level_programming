#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as e:
        print(f"Caught a name exception: {e}")
        raise  # Re-raise the caught exception
