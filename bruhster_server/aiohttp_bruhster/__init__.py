import os.path
import qtoml as toml

#open config with right path
DB_CONFIG_PATH = os.path.join('bruhster_server', 'config','db_config.toml')
WEB_CONFIG_PATH = os.path.join('bruhster_server', 'config','web_config.toml')

def load_config(path):
    with open(path, 'r') as f:
        config = toml.load(f)
        return config

def db_url_make(config):
    os.environ['DB_CONFIG_URL'] = 'postgresql://'+config['settings']['username']+':'+config['settings']['password']+'@'+config['settings']['host']+':'+config['settings']['port']+'/'+config['settings']['database']
    return

def make_config_env_var(config):
    keys = dict.keys(config['settings'])
    for i in keys:
        os.environ[i] = config['settings'][i]
    return

db_url_make(load_config(DB_CONFIG_PATH))

make_config_env_var(load_config(WEB_CONFIG_PATH))
