#!/usr/bin/env python3
"""module for 2-measure_runtime.py"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """a func that measures the runtime"""
    begin = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    elapsed_time = end - begin
    return elapsed_time / n
