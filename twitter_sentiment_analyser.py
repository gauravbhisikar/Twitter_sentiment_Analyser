import tweepy
import pandas as pd 
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer




consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.search('Artificial Intelligence', count=200)

data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

print(data.head(10))


print(tweets[0].created_at)


sia = SentimentIntensityAnalyzer()


listy = []

for index, row in data.iterrows():
  ss = sia.polarity_scores(row["Tweets"])
  listy.append(ss)
  
se = pd.Series(listy)
data['polarity'] = se.values

print(data.head(100))

