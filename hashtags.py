#!/usr/bin/env python3

"""
Generate an edge list for retweets.
"""

import csv
import sys
import json
import fileinput

out = csv.writer(sys.stdout)

for line in fileinput.input():
    try:
        tweet = json.loads(line)
    except:
        continue
    user = tweet['user']['screen_name']
    hashtags = [ht['text'].lower() for ht in tweet['entities']['hashtags']]
    if len(hashtags) > 0:
        out.writerow([user, ' '.join(hashtags)])
