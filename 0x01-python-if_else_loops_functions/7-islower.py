#!/usr/bin/env python3

def islower(c):
    """
    Returns True if c is lowercase, False otherwise.
    """
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False
