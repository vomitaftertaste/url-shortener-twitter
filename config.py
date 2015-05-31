
conf = {
    'DATABASE':'data.db',
    'TWITTER_APP_KEY':'',
    'TWITTER_APP_SECRET':'',
    'TWITTER_OAUTH_TOKEN': '',
    'TWITTER_OAUTH_TOKEN_SECRET': '',
    'DOMAIN_REDIRECT':''
}

def get_config(key):
    return conf[key]