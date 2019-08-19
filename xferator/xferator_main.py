import argparse
import asyncio
from asyncio import Queue
import httpx
import requests
import aiohttp


async def get(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_from(src,dest):

    async with aiohttp.session.get(src) as resp:
    with open(dest, 'wb') as fd:
        while True:
            chunk = await resp.content.read(8192)
            if not chunk:
                break
            fd.write(chunk)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--from", help="Copy from this location")
    parser.add_argument("--to", help="Copy to this location")
    parser.add_argument("--from_authenticate", help="Authentication for --from")
    parser.add_argument("--to_authenticate", help="Authentication for --to")

    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
