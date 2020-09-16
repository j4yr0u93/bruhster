import asyncio
import asyncpg
import sqlalchemy
import gino
import datetime
import time
import sys
import subprocess
from aiohttp import web
from aiohttp_bruhster.routes import setup_routes
from aiohttp_bruhster import web_config, DB_CONFIG_URL
#from aiohttp_session import setup, get_session, session_middleware
#from aiohttp_session.cookie_storage import EncryptedCookieStorage


#start web server
app = web.Application()
setup_routes(app)
web.run_app(app, host=web_config['WEB_HOST'], port=web_config['WEB_PORT'])
