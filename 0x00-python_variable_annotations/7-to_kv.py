#!/usr/bin/env python3
"""a module Complex types - string and int/float to tuple"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """a func that returns a tuple"""
    return ((k, (v ** 2)))
