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
out.writerow(['created', 'retweeter', 'retweeted'])

for line in fileinput.input():
    try:
        tweet = json.loads(line)
    except:
        continue

    src = tweet['user']['screen_name']

    dst = set()
    if 'retweeted_status' in tweet:
        tweet = tweet['retweeted_status']
        dst.add(tweet['user']['screen_name'])

    if 'extended_tweet' in tweet:
        mentions = tweet['extended_tweet']['entities']['user_mentions']
    else:
        mentions = tweet['entities']['user_mentions']

    for mention in mentions:
        dst.add(mention['screen_name'])

    created = arrow.get(tweet['created_at'], "MMM DD HH:mm:ss +0000 YYYY")

    out.writerow([
        created.strftime('%Y-%m-%d %H:%M:%S'),
        src,
        ' '.join(dst)
    ])
