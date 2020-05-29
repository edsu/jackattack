# jackattack

Watching tweets sent to @jack or @yoyoel after the decision to fact check one of
Trump's tweets.

* collect.py - collects tweets that mention @jack or @yoyoel from the filter stream
* ids.txt - a list of tweet ids collected so far
* hashtags.py - generate a CSV of users and hashtags
* mentions.py - generate a list of users and who they are mentioning
* retweets.py - retweet network (with timestamp for partitioning)
* segment.py - segment a csv into time buckets

## Run

First you'll need some dependencies:

    pip install -r requirements.txt

Then tell twarc about your Twitter API keys:

    twarc configure
   
Then you can collect the tweets:

    ./collect.py > stream.jsonl

After a while, or while it's running you can generate an edge list of replies
that you can visualize (in Gephi):

    ./mentions.py stream.jsonl > mentions.csv

Or you can look at the retweets:

    ./retweets.py stream.jsonl > retweets.csv
