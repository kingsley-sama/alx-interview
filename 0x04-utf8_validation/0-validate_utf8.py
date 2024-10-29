#!/usr/bin/python3
"""This module defines the validUTF8 function."""


def validUTF8(data):
    """Method that determines if a given
    data set represents a valid UTF-8 encoding."""
    try:
        by_list = bytes(data)
        by_list.decode('utf-8')
        return True
    except ValueError:
        return False
    except UnicodeDecodeError:
        return False
