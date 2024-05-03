#!/usr/bin/env python3
"""100-safe_first_element.py module"""
import typing


def safe_first_element(
    lst: typing.Sequence[typing.Any],
) -> typing.Union[typing.Any, None]:
    """a func that duck typing - first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
