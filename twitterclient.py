import re
from os import environ, path
from twython import Twython, TwythonError
from textblob import TextBlob

class TwitterBot(object):
    '''
    Twitter Bot to retrive tweets related to particult hashtag for sentiment analysis
    '''

    def __init__(self):
        TWITTER_API_KEY = environ['Twitter_API_Key']
        TWITTER_APP_KEY_SECRET = environ['Twitter_API_Key_Secret']
        TWITTER_ACCESS_TOKEN = environ['Twitter_OAuth_Token']
        TWITTER_ACCESS_TOKEN_SECRET = environ['Twitter_Access_Token_Secret']

        try:
            self.tw = Twython(
                app_key=TWITTER_API_KEY,
                app_secret=TWITTER_APP_KEY_SECRET,
                oauth_token=TWITTER_ACCESS_TOKEN,
                oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
        except:
            print("Error: Twitter Authentication Failed")
    
    def sanitize_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_tweet_sentiment(self, tweet):
        sentiment_analysis = TextBlob(self.sanitize_tweet(tweet))
        if sentiment_analysis.sentiment.polarity > 0:
            return 'positive'
        elif sentiment_analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 200):
        tweets = []

        try:
            searched_tweets = self.tw.search(q = query, count = count)['statuses']

            for tweet in searched_tweets:
                parse_tweet = {}

                parse_tweet['id'] = tweet['id_str']
                parse_tweet['text'] = tweet['text']
                parse_tweet['sentiment'] = self.analyze_tweet_sentiment(tweet['text'])

                if tweet['retweet_count'] > 0:
                    if parse_tweet not in tweets:
                        tweets.append(parse_tweet)
                else:
                    tweets.append(parse_tweet)
            return tweets
        except TwythonError as e:
            print("Error: ", str(e))
    