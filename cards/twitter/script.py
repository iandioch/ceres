#!/usr/bin/python3

import json

import tweepy

if __name__ == '__main__':
    d = None
    with open('config.hidden.json', 'r') as f:
        d = json.load(f)
    auth = tweepy.OAuthHandler(d['consumer_key'], d['consumer_secret'])
    auth.set_access_token(d['access_token'], d['access_token_secret'])

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        with open('data.json', 'w') as f:
            f.write(json.dumps(tweet._json))
            break
