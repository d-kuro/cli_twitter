#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# twitterLib
from twitter import *
# authKey
from auth import *
# util
from util import *
# message
from constant_tweet_template import *
import traceback
# KVS
from kvs import *
# exception
from exception import *

# show Timeline REST API
# [OPTION] [COUNT(DEFAULT 10)]
def show_timeline(args):
    count = 10

    try:
        if len(args) == 1:
            count = args[0]
            if not count.isdigit():
                raise OptionError

        twitter = TwitterGet().twitter_instance

        # REST API
        tweets = twitter.statuses.home_timeline(count=count)

        # print Tweet
        print_tweet(tweets)
    except OptionError as e:
        print(e.error_message)
    except Exception as e:
        raise OtherError

# show Mydata REST API
def show_mydata():
    try:
        twitter = TwitterGet().twitter_instance

        # REST API
        my_data = twitter.account.verify_credentials()

        # print MyData
        print_my_data(my_data)
    except Exception as e:
        raise OtherError

# get My ScreenName REST API
def get_my_screen_name():
    try:
        twitter = TwitterGet().twitter_instance

        # REST API
        my_data = twitter.account.verify_credentials()
        screen_name = "[@" + my_data["screen_name"] + "] $ "

        return screen_name
    except Exception as e:
        raise OtherError

# search Tweets
# [OPTIONS] [KEYWORD] [COUNT(DEFAULT 10)]
def search_tweets(args):
    count = 10

    try:
        if len(args) == 1:
            q = args[0]
        elif len(args) == 2:
            q = args[0]
            count = args[1]
            if not count.isdigit():
                raise OptionError
        else:
            raise OptionError

        twitter = TwitterGet().twitter_instance

        # REST API
        search_tweets = twitter.search.tweets(q=q, count=count)

        #print(search_tweets)
        tweets = search_tweets["statuses"]

        # print Tweet
        print_tweet(tweets)
    except OptionError as e:
        print(e.error_message)
    except Exception as e:
        raise OtherError

# post Tweet
# [OPTION] [*POSTTEXT] [REPLYtoID]
def post_tweet(args):
    in_reply_to_status_id = None
    try:
        if len(args) == 1:
            status = args[0]
        elif len(args) == 2:
            status = args[0]
            id = args[1]
            if not id.isdigit():
                raise OptionError
            export = shelve_export(id)
            in_reply_to_status_id = export["id"]
        else:
            raise OptionError

        twitter = TwitterGet().twitter_instance

        # REST API
        tweet = twitter.statuses.update(status=status, in_reply_to_status_id=in_reply_to_status_id)

        # print Tweet
        print_action_tweet(tweet)
    except OptionError as e:
        print(e.error_message)
    except Exception as e:
        raise OtherError

# retweet
# [OPTION] [*ID]
def retweet(args):
    try:
        if len(args) == 1:
            id = args[0]
            if not id.isdigit():
                raise OptionError
            export = shelve_export(id)
            id = export["id"]
        else:
            raise OptionError

        twitter = TwitterGet().twitter_instance

        # REST API
        tweet = twitter.statuses.retweet(id=id)

        # print Tweet
        print_action_tweet(tweet)
    except OptionError as e:
        print(e.error_message)
    except Exception as e:
        raise OtherError
