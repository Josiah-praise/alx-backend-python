#!/usr/bin/python3
"""
Type Checking
"""
from typing import  Iterable, List, TypeVar, Union

T = TypeVar('T')


def zoom_array(lst: Iterable[T], factor: Union[int, float]= 2) -> List[T]:
    factor = int(factor)
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
