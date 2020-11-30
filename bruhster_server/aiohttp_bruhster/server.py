import asyncio
import asyncpg
import sqlalchemy
import gino
import datetime
import time
import sys
import os
import subprocess
import base64
import spotipy
import uuid
from cryptography import fernet
from aiohttp import web
from aiohttp_session import setup, get_session, session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiohttp_bruhster.routes import setup_routes
from aiohttp_bruhster import web_config


#start web server with sessions(aes cookies)
async def handler(request):
    session = await get_session(request)
    last_visit = session['last_visit'] if 'last_visit' in session else None
    session['last_visit'] = time.time()
    text = 'Last visited: {}'.format(last_visit)
    return web.Response(text=text)

def make_app():
    app = web.Application()
    # secret_key must be 32 url-safe base64-encoded bytes
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))
    setup_routes(app)
    app.router.add_get('/', handler)
    return app

web.run_app(make_app(), host=web_config['WEB_HOST'], port=web_config['WEB_PORT'])
