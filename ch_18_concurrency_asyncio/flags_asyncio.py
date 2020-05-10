""" asyncio has changes a lot, so I'll be including a tutorial found outside the book in this module later """

# import asyncio
# import aiohttp
#
# from ch_17_concurrency_futures.flags import BASE_URL, save_flag, show, main
#
#
# async def get_flag(cc):
#     url = f'{BASE_URL}/{cc.lower()}/{cc.lower}.gif'
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             await resp.read()
#
#
# async def download_one(cc):
#     image = await get_flag(cc)
#     show(cc)
#     save_flag(image, cc.lower() + '.gif')
#     return cc
#
#
# def download_many(cc_list):
#     loop = asyncio.get_event_loop()
#     to_do = [download_one(cc) for cc in sorted(cc_list)]
#     wait_coro = asyncio.wait(to_do)
#     res, _ = loop.run_until_complete(wait_coro)
#     loop.close()
#
#     return len(res)
#
#
# if __name__ == '__main__':
#     main(download_many)
#

