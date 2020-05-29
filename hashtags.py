#!/usr/bin/env python3

"""
Generate an edge list for retweets.
"""

import csv
import sys
import json
import arrow
import fileinput

out = csv.writer(sys.stdout)
out.writerow(['created', 'user', 'hashtags'])

for line in fileinput.input():
    try:
        tweet = json.loads(line)
    except:
        continue
    user = tweet['user']['screen_name']
    hashtags = [ht['text'].lower() for ht in tweet['entities']['hashtags']]
    if len(hashtags) > 0:
        created = arrow.get(tweet['created_at'], "MMM DD HH:mm:ss +0000 YYYY")
        out.writerow([
            created.strftime('%Y-%m-%d %H:%M:%S'),
            user,
            ' '.join(hashtags)
        ])
