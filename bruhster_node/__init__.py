#init
import os.path
import qtoml as toml
from decouple import config

#spotify API env vars
SPOTIFY_API_ID = config('SPOTID')
SPOTIFY_API_SECRET = config('SPOTSEC')
#twitch API env vars
TWITCH_API_ID = config('TWITID')
TWITCH_API_SECRET = config('TWITSEC')
#discord API env vars
DISCORD_API_ID = config('DISCID')
DISCORD_API_SECRET = config('DISCSEC')

#need to define way to access db and then use some sort of token or id to load node config in node_worker.py
