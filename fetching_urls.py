#!/usr/bin/python3
"""
Fetching Urls at once
"""

import aiohttp
import asyncio
import requests
import time

url: list[str]= []
start = time.perf_counter()
for i in range(1, 5001):
    url.append(f"https://jsonplaceholder.typicode.com/photos/{i}")

async def fetch(session: aiohttp.ClientSession, _url: str) -> None:
    """
    Asynchronously makes a get request to _url and prints the response
    """
    async with session.get(_url) as response:
        return await response.json()


async def multiple_req(urlList: list[str]) -> None:
    """
    concurrently makes a request to all urls and logs the result
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, each) for each in urlList]
        
        for result in await asyncio.gather(*tasks):
            print(result)
        print(time.perf_counter() - start)
        print(f"==================================={len(tasks)}================================")

if __name__ == "__main__":
    asyncio.run(multiple_req(url))
