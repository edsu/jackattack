# jackattack

Watching tweets sent to @jack or @yoyoel after the decision to fact check one of
Trump's tweets.

* collect.py - collects tweets that mention @jack or @yoyoel from the filter stream
* ids.txt - a list of tweet ids collected so far
* network.py - generate a edge list suitable for Gephi
* network.csv - output of network.py 

## Run

First you'll need some dependencies:

    pip install -r requirements.txt

Then tell twarc about your Twitter API keys:

    twarc configure
   
Then you can collect the tweets:

    ./collect.py > stream.jsonl

After a while, or while it's running you can generate an edge list you can 
visualize (in Gephi):

    ./network.py stream.jsonl > network.csv
