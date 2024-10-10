#!/usr/bin/env python3
"""
we are making some ducks
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    iterable indicates that the arg is an iterable object.
    Sequence to specify that each element of the
    iterable is a sequence.
    """
    return [(i, len(i)) for i in lst]
