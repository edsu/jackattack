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

    # user names
    retweeter = tweet['user']['screen_name']
    retweeted = tweet['retweeted_status']['user']['screen_name']

    # elapsed time between tweet & retweet
    time_retweet = arrow.get(tweet['created_at'], fmt)
    time_original = arrow.get(tweet['retweeted_status']['created_at'], fmt)
    rttime = time_retweet - time_original

    # elapsed time between the retweet and the retweeter's account creation
    retweeter_created = arrow.get(tweet['user']['created_at'], fmt)
    retweeter_age = time_retweet - retweeter_created

    # elapsed time between the original tweet and their account creation
    retweeted_created = arrow.get(tweet['retweeted_status']['user']['created_at'], fmt)
    retweeted_age = time_original - retweeted_created

    out.writerow([
        retweeter,
        retweeted,
        rttime.total_seconds(),
        retweeter_age.days,
        retweeted_age.days
    ])


 
