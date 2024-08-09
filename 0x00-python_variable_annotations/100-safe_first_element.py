#!/usr/bin/python3
"""
Duck typing - first element of a sequence
"""
from typing import Sequence, Optional, TypeVar

# The types of the elements of the input are not know
T = TypeVar('T')


def safe_first_element(lst: Sequence[T]) -> Optional[T]:
    """
    Duck Typing - first element of a sequence
    """
    if lst:
        return lst[0]
    return "string"
