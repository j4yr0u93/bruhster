import os.path
import qtoml as toml

#open config with right path
DB_CONFIG_PATH = os.path.join('config','db_config.toml')
WEB_CONFIG_PATH = os.path.join('config','web_config.toml')

def load_config(path):
    with open(path, 'r') as f:
        config = toml.load(f)
        return config

def db_url_make(config):
    globals()['DB_CONFIG_URL'] = 'postgresql://'+config['settings']['username']+':'+config['settings']['password']+'@'+config['settings']['host']+':'+config['settings']['port']+'/'+config['settings']['database']
    return

db_url_make(load_config(DB_CONFIG_PATH))

globals()['web_config'] = load_config(WEB_CONFIG_PATH)['settings']
