#!/usr/bin/env python

"""
Generate a CSV file for Gephi.
"""

import csv
import json

out = csv.writer(open("network.csv", "w"))


for line in open('stream.jsonl'):
    tweet = json.loads(line)
    src = tweet['user']['screen_name']

    user_mentions = tweet['entities']['user_mentions']
    if 'extended_tweet' in tweet:
        user_mentions = tweet['extended_tweet']['entities']['user_mentions']

    # multiple destinations are space separated (gephi likes this)    
    dst = ' '.join([u['screen_name'] for u in user_mentions])

    out.writerow([src,dst])




    



