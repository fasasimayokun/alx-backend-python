#!/usr/bin/env python3
"""module for 1-async_comprehension.py"""
import typing

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> typing.List[float]:
    """a func async Comprehensions"""
    return [i async for i in async_generator()]
