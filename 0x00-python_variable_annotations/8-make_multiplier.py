#!/usr/bin/python3
"""
Complex-types
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    retuns a function that multiplies a float by a multiplier
    """

    def func(mul: float) -> float:
        """
        multiply mul by multipier
        """
        return float(mul * multiplier)
