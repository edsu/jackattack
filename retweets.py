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
    if 'retweeted_status' in tweet:
        created = arrow.get(tweet['created_at'], "MMM DD HH:mm:ss +0000 YYYY")
        src = tweet['user']['screen_name']
        dst = tweet['retweeted_status']['user']['screen_name']
        out.writerow([
            created.strftime('%Y-%m-%d %H:%M:%S'),
            src,
            dst
        ])
