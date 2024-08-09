#!/usr/bin/python3
"""
Fetching Urls with in batches
"""

import aiohttp
import asyncio
import requests
import time
from typing import Generator, Any

# url: list[str]= []
start = time.perf_counter()
# for i in range(1, 5001):
#     url.append(f"https://jsonplaceholder.typicode.com/photos/{i}")


def batch_urls(batch: int, total: int,
               url: str) -> Generator[list[str], Any, None]:
    """
    returns a list of batched urls
    """
    _urls: list[str] = []
    _start: int = 1
    end = _start + batch
    while _start < total:
        _urls.clear()
        for each in range(_start, end):
            _urls.append(f"{url}/{each}")
        _start = end
        end = _start + batch
        yield _urls
    yield []


async def fetch(session: aiohttp.ClientSession, _url: str):
    """
    Asynchronously makes a get request to _url and prints the response
    """
    async with session.get(_url) as response:
        if response.status == 200:
            return await response.json()
        return {"Error": 404}


async def multiple_req(url: str) -> None:
    """
    concurrently makes a request to all urls and logs the result
    """
    async with aiohttp.ClientSession() as session:
        # tasks = [asyncio.create_task(fetch(session, each)) for each in batch_urls(500, 5000, url)]
        count = 1
        for url_batch in batch_urls(500, 5000, url):
            if url_batch:
                tasks = [fetch(session, url) for url in url_batch]
                print(
                    f"===================================Batch {count}================================"
                )
                [print(result) for result in await asyncio.gather(*tasks)]
            count += 1

        print(time.perf_counter() - start)


if __name__ == "__main__":
    asyncio.run(multiple_req("https://jsonplaceholder.typicode.com/photos"))
