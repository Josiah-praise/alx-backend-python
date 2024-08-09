#!/usr/bin/python3
"""
Basic Level
"""
import ayncio

async def greet():
    """
    Simple Coroutine
    """
    await asyncio.sleep(1)
    print("Hello World")

