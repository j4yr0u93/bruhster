from aiohttp import web


async def index(request):
    return web.Response(text='Hello Aiohttp!')

async def test(request):
    return web.Response(text='Test was a big success')
