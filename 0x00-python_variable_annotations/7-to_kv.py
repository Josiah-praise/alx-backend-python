#!/usr/bin/python3
"""
Complex Types
"""

def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """
    a tuple of k and v
    """
    return (k, float(v**2))
