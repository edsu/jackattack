#!/usr/bin/env python

import sys
import pandas
import datetime

from pathlib import Path

csv_file = sys.argv[1]
output_dir = Path(csv_file.replace('.csv', '') + '-segments')

if not output_dir.is_dir():
    output_dir.mkdir()

df = pandas.read_csv(csv_file, parse_dates=['created'])
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

    segment = segment.drop('created', axis=1)
    segment_file = output_dir / '{}-{}.csv'.format(
        start.strftime('%Y%m%d%H%M%S'),
        end.strftime('%Y%m%d%H%M%S'),
    )

    segment.to_csv(segment_file, index=False, header=False)
    start = end

