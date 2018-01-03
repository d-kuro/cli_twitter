#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# twitterLib
from twitter import *

CONSUMER_KEY = "xxxxxxxxxx"
CONSUMER_SECRET_KEY = "xxxxxxxxxx"
ACCESS_TOKEN = "xxxxxxxxxx"
ACCESS_TOKEN_SECRET = "xxxxxxxxxx"

class Auth(object):
    def __init__(self):
        self.__auth = OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET_KEY)

    @property
    def auth(self):
        return self.__auth

class TwitterGet(Auth):
    def __init__(self):
        super().__init__()
        self.__twitter_instance = Twitter(auth=self.auth)

    @property
    def twitter_instance(self):
        return self.__twitter_instance

class StreamGet(Auth):
    def __init__(self):
        super().__init__()
        self.__stream_instance = TwitterStream(auth=self.auth,domain="userstream.twitter.com")

    @property
    def stream_instance(self):
        return self.__stream_instance


