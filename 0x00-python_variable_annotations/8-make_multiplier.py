#!/usr/bin/env python3
"""
iam here
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    iam here
    """
    def multiplier_func(x: float) -> float:
        return multiplier * x
    return multiplier_func
