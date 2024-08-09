#!/usr/bin/python3
"""
Complex-types
"""

def sum_list(input_list: list[float]) -> float:
    """
    returns the sum of input list
    """
    from functools import reduce
    return float(reduce(lambda a, b: a + b), input_list)
