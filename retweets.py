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
    tweet = json.loads(line)
    if 'retweeted_status' in tweet:
        src = tweet['user']['screen_name']
        dst = tweet['retweeted_status']['user']['screen_name']
        out.writerow([src,dst])




    



