import tweepy
import time

consumer_key = 'ZDyySngKigmSXfXqoYu0k5VvP'
consumer_secret = 'XbunRKnPSJsA689f20Yezu7dZ4Qde2wlJ2OOjoJo8bWHfjpxS2'
access_token = '1254713164274577408-lLZJsmD84HAA0R1p4eU47OklnuOirL'
access_token_secret = 'RhNh8gZXP5tyfuWuHQvGjsY8X0u1FhWnnJ6Fug9SmyiFC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()


def limit_hand(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


search_string = 'chelsea'
numbersOfTweets = 20

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try:
        tweet.favorite()
        print('I like that tweet')
    except tweepy.TweepError as er:
        print(er.reason)
    except StopIteration:
        break

# Generous Bot
# for followers in limit_hand(tweepy.Cursor(api.followers).items()):
#     print(followers.name)
