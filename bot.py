import json
import random
import os
import tweepy

client = tweepy.Client(
    consumer_key=os.environ["API_KEY"],
    consumer_secret=os.environ["API_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_SECRET"]
)

with open("hadiths.json", "r", encoding="utf-8") as f:
    hadiths = json.load(f)

hadith = random.choice(hadiths)

tweet = f"{hadith['texte']}\n\n{hadith['source']} n°{hadith['numero']}"

client.create_tweet(text=tweet)

print("Tweet publié :", tweet)
