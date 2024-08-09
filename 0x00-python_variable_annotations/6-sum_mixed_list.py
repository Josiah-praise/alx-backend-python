#!/usr/bin/python3
"""
Complex types
"""

def sum_mixed_list(mxd_lst: list[int, float]) -> float:
    """
    sums up mxd_lst
    """
    from functools import reduce
    return float(reduce(lambda a, b: a + b), mxd_lst)
