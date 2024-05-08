#!/usr/bin/env python3
"""module for 2-measure_runtime.py"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """an async func measure the total runtime and return it"""
    begin = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - begin
