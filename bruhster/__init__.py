#init
import os.path
import qtoml as toml

#open config with right path
CONFIG_PATH = os.path.join('bruhster', 'config', 'spotify_config.toml')


def load_config(path):
    with open(path, 'r') as f:
        config = toml.load(f)
        return config

def set_spot_env(config):
    os.environ['SPOTIPY_CLIENT_ID'] = config['spotify']['SPOTIPY_CLIENT_ID']
    os.environ['SPOTIPY_CLIENT_SECRET'] = config['spotify']['SPOTIPY_CLIENT_SECRET']
    os.environ['SPOTIPY_REDIRECT_URI'] = config['spotify']['SPOTIPY_REDIRECT_URI']
    return

set_spot_env(load_config(CONFIG_PATH))
