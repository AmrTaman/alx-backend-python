#!/usr/bin/env python3
"""
bessa is always making bess
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    iam maknig a none checker
    """
    if lst:
        return lst[0]
    else:
        return None
