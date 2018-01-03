#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# tweer時間整形用
import time, calendar
# printTemplate
from constant_tweet_template import *
# KVS
from kvs import *

# 日本時間に変換
def encode_date_jp(created_at):
    time_utc = time.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')
    unix_time = calendar.timegm(time_utc)
    time_local = time.localtime(unix_time)
    return time.strftime("%Y/%m/%d %H:%M:%S", time_local)

def print_tweet(tweets):
    # Client用ID => KVSのkeyに設定
    id = 0

    for tweet in tweets:

        if "created_at" in tweet.keys()\
            and "user" in tweet.keys()\
            and "text" in tweet.keys():

            id = id + 1
            created_at = encode_date_jp(tweet["created_at"])

            shelve_import(id, tweet)

            print(PRINT_TWEET_DATA.format(
                screen_name="@" + tweet["user"]["screen_name"],
                name=tweet["user"]["name"],
                created_at=created_at,
                id=id,
                text=tweet["text"]
            ))

def print_action_tweet(tweet, post=True):

    created_at = encode_date_jp(tweet["created_at"])

    if post:
        print(PRINT_POST_TWEET_DATA.format(
            screen_name="@" + tweet["user"]["screen_name"],
            name=tweet["user"]["name"],
            created_at=created_at,
            text=tweet["text"]
        ))
    else:
        print(PRINT_RT_TWEET_DATA.format(
            screen_name="@" + tweet["user"]["screen_name"],
            name=tweet["user"]["name"],
            created_at=created_at,
            text=tweet["text"]
        ))

def print_my_data(my_data):
    created_date = encode_date_jp(my_data["created_at"])

    print(PRINT_ACCOUNT_DATA.format(
        id=my_data["id"],
        screen_name="@" + my_data["screen_name"],
        name=my_data["name"],
        description=my_data["description"],
        followers_count=my_data["followers_count"],
        friends_count=my_data["friends_count"],
        favourites_count=my_data["favourites_count"],
        createdDate=created_date
        ))