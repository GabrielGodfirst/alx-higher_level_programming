#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print("Finally: Division completed")
