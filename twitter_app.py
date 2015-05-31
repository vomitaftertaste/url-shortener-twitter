from twython import *
from models import *
from config import get_config
from time import sleep
from twitter_url_service import *

delay = 60 #seconds
twitter = TwitterUrlService()

def update_last_processed(value):
    last_processed = KeyValueItem.get_or_create(key='last_processed')[0]
    last_processed.value = value
    last_processed.save()

def shorten(full_url):
    return get_config('DOMAIN_REDIRECT') + '/' + 'xyzabc'
  
def process_mentions(mentions):
    for mention in reversed(mentions):
        if len(mention['entities']['urls']) > 0:
            urls = []
            for url in mention['entities']['urls']:
                urls.append({
                    'full':url['expanded_url'],
                    'short':shorten(url['expanded_url']),
                    'display':url['display_url'],
                    't.co':url['url']
                })
            twitter.post_shortened_urls(mention, urls)
        print str(mention['id']) + ' processed...'
        update_last_processed(str(mention['id']))
        
if __name__ == '__main__':
    while True:
        mentions = twitter.get_mentions_timeline()
        if len(mentions) > 0:
            process_mentions(mentions)
        sleep(delay)
        