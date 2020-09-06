#kinky liberals
import asyncio
import asyncpg
import aiohttp
import datetime
import time
import sys
import subprocess
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#im fast as fug boi but not on windows
#asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

#set client token
spotify_client = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

#asyncpg connection to postgres server
#async def musicdb_connect():
#    conn = await asyncpg.connect(user='user', password='password',
#                                 database='database', host='127.0.0.1')
#    values = await conn.fetch('''SELECT * FROM mytable''')
#    await conn.close()
#
#loop = asyncio.get_event_loop()
#loop.run_until_complete(run())


#main
def main():
    print(spotify_client.search(q='apartment young the giant', limit=1, type='track'))
    time.sleep(5)
    return
