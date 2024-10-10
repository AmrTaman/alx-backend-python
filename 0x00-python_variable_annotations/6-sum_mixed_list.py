#!/usr/bin/env python3
"""
we are summing lists
"""
from typing import List, Union


def sum_mixed_list(lst: List[Union[int, float]]) -> float:
    """
    summing up int and floats
    """
    return sum(lst)
