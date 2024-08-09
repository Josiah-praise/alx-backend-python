#!/usr/bin/python3
"""
Let's duck type an iterable object
"""
from typing import Iterable, Callable, Sequence

def element_length(lst: Iterable[Sequence]) -> list[tuple[Sequence, int]]:
    """
    returns a list of tuples
    """
    return [(i, len(i)) for i in lst]
