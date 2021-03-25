import tweepy
import time

consumer_key = 
consumer_secret =
access_token = 
access_token_secret = 


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)


search1 = "India"
search2 = "Ironman"
no_of_tweets1 = 2
no_of_tweets2 = 2



for tweet in tweepy.Cursor(api.search, search1).items(no_of_tweets1):
    try:
      tweet.favorite()
      print("liked the tweet")
    except tweepy.TweepError as e:
      print(e.reason)
    except StopIteration:
      break


for tweet in tweepy.Cursor(api.search, search2).items(no_of_tweets2):
  try:
    tweet.retweet()
    print("retweeted the tweet")
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break
