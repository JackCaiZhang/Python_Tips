import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['https://bejing.anjuke.com/?from=HomePage_City', 
            'https://shanghai.anjuke.com/?from=HomePage_City', 
            'https://guangzhou.anjuke.com/?from=HomePage_City',
            'https://shenzhen.anjuke.com/?from=HomePage_City']
    tasks = [fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())