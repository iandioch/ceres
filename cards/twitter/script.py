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

    public_tweets = api.user_timeline(id='iandioch')
    for tweet in public_tweets:
        with open('data.json', 'w') as f:
            d = tweet._json
            d['html'] = ' '.join(['<a href="{}">{}</a>'.format(s, s) if s[:4] == 'http' else s for s in tweet.text.split()])
            d['url'] = 'https://twitter.com/iandioch/status/' + tweet.id_str
            f.write(json.dumps(d, indent=4))
            break
