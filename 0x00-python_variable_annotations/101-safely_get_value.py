#!/usr/bin/env python3
"""
module
"""
from typing import Mapping, TypeVar, Any, Union
T = TypeVar('T')


def safely_get_value(
                    dct: Mapping,
                    key: Any,
                    default: Union[T, None]) -> Union[Any, T]:
    """
    we are using typevar
    """
    if key in dct:
        return dct[key]
    else:
        return default
