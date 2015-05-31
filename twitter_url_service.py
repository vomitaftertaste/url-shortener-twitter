from twython import *
from config import *
from models import *
import pickle

class TwitterUrlService():
    def __init__(self, twython_object=None):
        if twython_object is None:
            self.twython_object = Twython(get_config('TWITTER_APP_KEY'),get_config('TWITTER_APP_SECRET'),get_config('TWITTER_OAUTH_TOKEN'),get_config('TWITTER_OAUTH_TOKEN_SECRET'))
        else:        
            self.twython_object = twython_object
        self.tweet_limit = 144
    
    def get_last_mention(self):
        return KeyValueItem.get_or_create(key='last_processed',defaults={'value':'1'})[0].value
    
    def get_mentions_timeline_online(self, all_mentions=False):
        if all_mentions:
            return self.twython_object.get_mentions_timeline()
        else:
            return self.twython_object.get_mentions_timeline(since_id=self.get_last_mention())
    
    def get_mentions_timeline_offline(self):
        return pickle.load(open('mentions.p','rb'))
        
    def get_mentions_timeline(self):
        return self.get_mentions_timeline_offline()
    
    def get_url_presentation_format(self, first_url, second_url):
        return first_url + ' -> ' + second_url + '\n'
    
    def construct_reply_texts(self, request_tweet, urls):
        reply_texts = []
        reply_text = "Hi @" + request_tweet['user']['screen_name'] + '\n'
        reply_text += "Your shortened urls:\n"
        current_len = len(reply_text)
        for url in urls:
            if current_len + len(self.get_url_presentation_format(url['t.co'],url['short'])) > self.tweet_limit:
                reply_texts.append(reply_text)
                reply_text = ""
                current_len = 0
            reply_text += self.get_url_presentation_format(url['display'],url['short'])
            current_len += len(self.get_url_presentation_format(url['t.co'],url['short']))
        reply_texts.append(reply_text)
        return reply_texts
    
    def post_shortened_urls_offline(self, request_tweet, reply_texts):
        for idx, reply in enumerate(reply_texts):
            print idx
            print reply.encode('utf-8')
        
    def post_shortened_urls_online(self, request_tweet, reply_texts):
        self.twython_object.update_status(status=construct_reply_text(request_tweet, urls), in_reply_status_id=request_tweet['id'])
    
    def post_shortened_urls(self, request_tweet, urls):
        self.post_shortened_urls_offline(request_tweet, self.construct_reply_texts(request_tweet, urls))
        