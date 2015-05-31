from twython import *
from config import *
from models import *

class TwitterUrlService():
    def __init__(self, twython_object=None):
        if twython_object is None:
            self.twython_object = Twython(get_config('TWITTER_APP_KEY'),get_config('TWITTER_APP_SECRET'),get_config('TWITTER_OAUTH_TOKEN'),get_config('TWITTER_OAUTH_TOKEN_SECRET'))
        else:        
            self.twython_object = twython_object
    
    def get_last_mention(self):
        return KeyValueItem.get_or_create(key='last_processed',defaults={'value':'1'})[0].value
    
    def get_mentions_timeline(self):
        return self.twython_object.get_mentions_timeline(since_id=self.get_last_mention())
    
    def construct_reply_text(self, request_tweet, urls):
        reply_text = "Hi @" + request_tweet['user']['screen_name'] + '\n'
        reply_text += "Your shortened urls:\n"
        for url in urls:
            reply_text += urls['display'] + ' -> ' + urls['short'] + '\n'
        return reply_text
    
    def post_shortened_urls(self, request_tweet, urls):
        self.twython_object.update_status(status=construct_reply_text(request_tweet, urls), in_reply_status_id=request_tweet['id'])
        