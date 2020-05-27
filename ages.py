#!/usr/bin/env python3


"""
Caculate times related to retweets.
"""

import csv
import sys
import json
import arrow
import fileinput

fmt = "MMM DD HH:mm:ss +0000 YYYY"
out = csv.writer(sys.stdout)
out.writerow([
    'retweeter',
    'retweeted',
    'retweet_time',
    'retweeter_age',
    'retweeted_age'
])

for line in fileinput.input():
    tweet = json.loads(line)

    if 'retweeted_status' not in tweet:
        continue

    retweeter = tweet['user']['screen_name']
    retweeted = tweet['retweeted_status']['user']['screen_name']

    time_retweet = arrow.get(tweet['created_at'], fmt)
    time_original = arrow.get(tweet['retweeted_status']['created_at'], fmt)
    rttime = time_retweet - time_original

    retweeter_age = time_retweet - arrow.get(tweet['user']['created_at'], fmt)
    retweeted_age = time_original - arrow.get(tweet['retweeted_status']['user']['created_at'], fmt)

    out.writerow([
        retweeter,
        retweeted,
        rttime.seconds,
        retweeter_age.seconds,
        retweeted_age.seconds
    ])


 
