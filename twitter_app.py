from twython import *
from models import *
from config import get_config
from time import sleep
from twitter_url_service import *

delay = 60 #seconds
twitter = TwitterUrlService()

def update_last_processed(value):
    last_processed = KeyValueItem.get_or_create(key='last_processed')
    last_processed.value = value
    last_processed.save()

def shorten(full_url):
    return get_config('DOMAIN') + '//' + 'xyzabc'
  
def process_mentions(mentions):
    for mention in reversed(mentions):
        if len(mention['entities']['url']) > 0:
            urls = []
            for url in mention['entities']['url']:
                urls.append({
                    'full':mention['entities']['url']['expanded_url'],
                    'short':shorten(mention['entities']['url']['expanded_url']),
                    'display':mention['entities']['url']['display_url']
                })
            twitter.post_shortened_urls(mention, urls)
        update_last_processed(mention['id'])
        
if __name__ == '__main__':
    while True:
        mentions = twitter.get_mentions_timeline()
        if len(mentions) > 0:
            process_mentions(mentions)
        sleep(delay)
        