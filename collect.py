#!/usr/bin/env python3

"""
Listen for tweets mentioning particular users.
"""

import json
import twarc

twitter = twarc.Twarc()
users = ['jack', 'yoyoel']

for tweet in twitter.filter(','.join(users)):

    # if it's > 140 chars look for the users in the extended_tweet 
    if 'extended_tweet' in tweet:
        user_mentions = tweet['extended_tweet']['entities']['user_mentions']
    else:
        user_mentions = tweet['entities']['user_mentions']

    found = False
    for mention in user_mentions:
        if mention['screen_name'].lower() in users:
            found = True
    if found:
        print(json.dumps(tweet))
