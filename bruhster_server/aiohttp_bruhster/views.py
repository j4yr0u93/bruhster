from aiohttp import web
from aiohttp_bruhster import spotify_oauth


async def index(request):
    return web.Response(text='Hello Aiohttp!')

async def moneyshot(request):
    async with aiohttp.ClientSession() as session:
        async with session.get('') as resp:
