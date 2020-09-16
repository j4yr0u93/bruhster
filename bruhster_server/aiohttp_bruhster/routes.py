from aiohttp_bruhster.views import index, test


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/test', test)
    return
