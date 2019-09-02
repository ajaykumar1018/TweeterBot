from random import choice
import tweepy
import json

with open('twitter_auth.json') as file:
    secrets = json.load(file)

auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_token_secret'])

twitter = tweepy.API(auth)

status = ['Valar Morghulis World!', 'Dracarys', 'Valar Doharis', 'Dragon is not a Slave', 'A lot can happen between now and never','Winter is coming', 'Fire and Blood', 'Khaleesi', 'You know nothing Jon Snow', 'The North never forgives']

def send_tweet():
    twitter.update_with_media('camerty.jpg', choice(status))
    print("Photo Uploaded")

send_tweet()
