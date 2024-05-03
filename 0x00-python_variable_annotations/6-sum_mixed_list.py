#!/usr/bin/env python3
"""a module Complex types - mixed list"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """a func that returns their sum as a float"""
    return (sum(mxd_lst))
