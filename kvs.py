#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# KVS
import shelve

FILENAME = 'shelve_data/tweet_data.db'

def shelve_import(id, tweet):
    try:
        kvs = shelve.open(FILENAME)
        kvs[str(id)] = tweet
        kvs.close()
    except Exception as e:
        print(e)

def shelve_export(id):
    try:
        kvs = shelve.open(FILENAME)
        return_data = kvs[str(id)]
        kvs.close()
        return return_data
    except Exception as e:
        print(e)