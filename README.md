# Dev Twitter Sentiment Analytics Bot

A hobbyist twitter bot designed to retrive batches of tweets based on a particular hashtag and analyze the user sentiment of each tweet.
This is a general learning project I am pursuing for understanding the Twitter API and data anlytics concepts.

### Tool Integrations

[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/malbert-design/twitter-sentiment-analysis-bot/?ref=repository-badge)

### Prerequisites

- Python 3
- Twitter developer API & secret keys, and OAuth access & secret tokens
- Twython
- TextBlob

### Configuration

You must configure your python environment to know your Twitter developer API and OAuth keys

- TWITTER_API_KEY = environ['Twitter_API_Key']
- TWITTER_APP_KEY_SECRET = environ['Twitter_API_Key_Secret']
- TWITTER_ACCESS_TOKEN = environ['Twitter_OAuth_Token']
- TWITTER_ACCESS_TOKEN_SECRET = environ['Twitter_Access_Token_Secret']

### Versions

- v0.0.1 (Alpha) - 2/8/2020: Initial publish of test Twitter API and sentiment analysis code

### Future Plans

- Identify trending topics/content in tweets related to the hashtag
- Identify common topics/words/phrases with positive or negative sentiments (hypothetical stage)
- Export reports of sentiment analysis
- Tweet reports to Twitter Bot account on manual or scheduled basis

### Acknowledgements

- Twitter for developer API - https://developer.twitter.com/
- Ryan McGrath for Twython API - https://twython.readthedocs.io/en/latest/
- Steven Loria for TextBlob API - https://textblob.readthedocs.io/en/dev/
- Communities on a variety of open-source coding boards & GitHub for research and learning material