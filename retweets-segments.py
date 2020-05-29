#!/usr/bin/env python

import pandas
import datetime

df = pandas.read_csv('retweets.csv', parse_dates=['created'])
df = df.sort_values('created', ascending=True)

start = df.created[0]
start = datetime.datetime(
    year=start.year,
    month=start.month,
    day=start.day,
    hour=start.hour
)

segment_num = 0
while True:
    segment_num += 1
    end = start + datetime.timedelta(hours=4)
    segment = df[(df['created'] >= start) & (df['created'] < end)]
    if len(segment) == 0:
        break
    segment
    segment.to_csv(
        'retweets-segments/{}-{}.csv'.format(
            start.strftime('%Y%m%d%H%M%S'),
            end.strftime('%Y%m%d%H%M%S'),
        ),
        index=False,
        columns=['retweeter', 'retweeted'],
        header=False
    )
    start = end

