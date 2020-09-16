import os.path
import qtoml as toml

#open config with right path
WEB_CONFIG_PATH = os.path.join('config','web_config.toml')
SPOTIFY_OAUTH_PATH = os.path.join('config', 'spotify_oauth.toml')

def load_config(path):
    with open(path, 'r') as f:
        config = toml.load(f)
        return config

def oauth_url_params_make(config):
    url_params = '?client_id=' + config['settings']['SPOTIFY_ID'] + '&response_type=code&redirect_uri=' + config['settings']['REDIRECT_URI']
    if config['settings']['OAUTH_STATE'] != '':
        url += '&state=' + config['settings']['OAUTH_STATE']
    url_params += '&scope='
    for i in config['settings']['OAUTH_STATE']:
        if config['settings']['OAUTH_STATE'][i] != len(config['settings']['OAUTH_STATE']) - 1:
            url_params += i + '%20'
        else:
            url_params += i
    #eventually change logic to if user is in user db then false otherwise true in case refresh token was flushed and move to user auth module
    #if config['settings']['SHOW_DIALOG'] == 'TRUE':
    #    url_params +=
    globals()['oauth_params'] = url_params
    return


globals()['web_config'] = load_config(WEB_CONFIG_PATH)['settings']

globals()['spotify_oauth'] = load_config(SPOTIFY_OAUTH_PATH)['settings']
