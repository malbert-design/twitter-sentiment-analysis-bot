from os import environ, path
from twitterclient import TwitterBot
import json, datetime, pymongo, sys, threading, time, requests

HASHTAG = environ['Hashtag']

# Run a search through twitter for specific hashtag and retrieve X number of tweets
tw = TwitterBot()
tweets = tw.get_tweets(HASHTAG, 200)

for tweet in tweets:
    print(tweet['id'], '\n', tweet['text'], '\n', tweet['sentiment'], '\n\n\n')

