from random_words import RandomNicknames, RandomWords
from models import *

def generate_random_sentence():
    return RandomWords().random_word() + RandomNicknames().random_nick(gender='u')

def is_url_exist(short_url):
    try:
        UrlData.get(short=short_url)
        return True
    except:
        return False

def sentence_shortener(full_url):
    short = generate_random_sentence()
    while is_url_exist(short):
        short = generate_random_sentence()
    UrlData.create(short=short, full=full_url)
    return get_config('DOMAIN_REDIRECT') + '/' + short
    
def test_shortener(full_url):
    return get_config('DOMAIN_REDIRECT') + '/' + 'xyzabc'
