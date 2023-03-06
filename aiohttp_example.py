import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.github.com/events') as resp:
            print("Status:", resp.status)
            print("Content-type:", resp.headers['content-type'])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
