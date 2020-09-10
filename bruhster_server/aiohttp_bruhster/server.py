from aiohttp import web
from aiohttp_bruhster.routes import setup_routes
import gino
import sqlalchemy as sa
from aiohttp_bruhster import web_config, DB_CONFIG_URL
from aiohttp_session import setup, get_session, session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage



#create db engine w/ gino
udb = gino.Gino()
async def main():
    udb_engine = await gino.create_engine(DB_CONFIG_URL)
    udb.bind = udb_engine

#user sessions as documented in server usage
async def handler(request):
    session = await get_session(request)
    last_visit = session['last_visit'] if 'last_visit' in session else None
    text = 'Last visited: {}'.format(last_visit)
    return web.Response(text=text)

def make_app():
    app = web.Application()
    # secret_key must be 32 url-safe base64-encoded bytes
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))
    app.router.add_route('GET', '/', handler)
    return app

web.run_app(make_app(), host=web_config['WEB_HOST'], port=web_config['WEB_PORT'])

app = web.Application()
setup_routes(app)
web.run_app(app, host=web_config['WEB_HOST'], port=web_config['WEB_PORT'])
