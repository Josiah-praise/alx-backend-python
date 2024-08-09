#!/usr/bin/python3
"""
More involved type annotations
"""
from typing import Mapping, Union, Optional, TypeVar

K = TypeVar("K")
D = TypeVar("D")
V = TypeVar("V")


def safely_get_value(dct: Mapping[K, V], key: K, default: Optional[D] = None) -> Union[V, Optional[D]]:
    if key in dct:
        return dct[key]
    else:
        return default
