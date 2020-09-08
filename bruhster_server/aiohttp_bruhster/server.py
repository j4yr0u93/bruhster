from aiohttp import web
from aiohttp_bruhster.routes import setup_routes
import gino
import sqlalchemy as sa
from aiohttp_bruhster import web_config, DB_CONFIG_URL



#create db engine w/ gino
udb = gino.Gino()
async def main():
    udb_engine = await gino.create_engine(DB_CONFIG_URL)
    udb.bind = udb_engine

app = web.Application()
setup_routes(app)
web.run_app(app, host=web_config['WEB_HOST'], port=web_config['WEB_PORT'])
