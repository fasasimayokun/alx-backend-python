#!/usr/bin/env python3
"""a module that Let's duck type an iterable object"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> (
        typing.List[typing.Tuple[typing.Sequence, int]]):
    """a func that returns a list"""
    return [(i, len(i)) for i in lst]
