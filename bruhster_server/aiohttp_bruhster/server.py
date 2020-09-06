from aiohttp import web
from routes import setup_routes
import gino
import sqlalchemy as sa


#create db engine
udb = gino.Gino()
async def main():
    udb_engine = await gino.create_engine(DB_CONFIG_URL)
    udb.bind = udb_engine
#e for Gino engine

app = web.Application()
setup_routes(app)
web.run_app(app, host='127.0.0.1', port=8080)
