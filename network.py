#!/usr/bin/env python3

"""
Generate a CSV file for Gephi.
"""

import csv
import sys
import json
import fileinput

out = csv.writer(sys.stdout)

for line in fileinput.input():
    tweet = json.loads(line)
    src = tweet['user']['screen_name']

    user_mentions = tweet['entities']['user_mentions']
    if 'extended_tweet' in tweet:
        user_mentions = tweet['extended_tweet']['entities']['user_mentions']

    # multiple destinations are space separated (gephi likes this)    
    dst = ' '.join([u['screen_name'] for u in user_mentions])

    out.writerow([src,dst])




    



