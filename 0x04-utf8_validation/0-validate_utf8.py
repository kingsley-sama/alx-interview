#!/usr/bin/python3
"""This module defines the validUTF8 function."""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Method that determines if a given
    data set represents a valid UTF-8 encoding."""
    if data:
        try:
            by_list = bytes(data)
            by_list.decode('utf-8')
            return True
        except ValueError:
            return False
        except UnicodeDecodeError:
            return False
