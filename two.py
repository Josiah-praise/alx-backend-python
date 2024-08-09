#!/usr/bin/python3
"""
Basic Level
"""

import asyncio

async def func1():
    await asyncio.sleep(2)
    print("Task 1")

async def func2():
    await asyncio.sleep(2)
    print("task 2")

async def main():
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())

    await task1

