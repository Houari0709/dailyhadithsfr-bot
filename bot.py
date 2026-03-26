import json
import random
import os
import tweepy

auth = tweepy.OAuth1UserHandler(
    os.environ["API_KEY"],
    os.environ["API_SECRET"],
    os.environ["ACCESS_TOKEN"],
    os.environ["ACCESS_SECRET"]
)

api = tweepy.API(auth)

with open("hadiths.json", "r", encoding="utf-8") as f:
    hadiths = json.load(f)

hadith = random.choice(hadiths)

tweet = f"{hadith['texte']}\n\n{hadith['source']} n°{hadith['numero']}"

api.update_status(tweet)

print("Tweet publié :", tweet)
