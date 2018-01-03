#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# accessTwitterAPI
from access_twitter_api import *
# constantMessage
from constant import *
from error_message import *
# exception
from exception import *
import traceback
# 独自コンソール用
import sys
import code
import os
import re

# コンソール
class TwitterConsole(code.InteractiveConsole):
    def __init__(self, local=None, filename="<console>"):
        code.InteractiveConsole.__init__(self, local, filename)

    def push(self, line):
        try:
            args = []
            # クォーテーションで囲まれている文字をsplitの対象外にする
            if re.search("[\"\'].*[\"\']", line):
                text_data = re.search("[\"\'].*[\"\']", line).group()
                text_data = re.sub("[\"\']", "", text_data)
                args.append(text_data)
                line = re.sub("[\"\'].*[\"\']", "", line)

            # スペースで分割
            line_data = line.split()
            for i, text in enumerate(line_data):
                if i == 0:
                    command = text
                else:
                    args.append(text)

            # 存在しないコマンドの場合は例外送出
            if command not in COMMAND_LIST:
                raise CommandError

            if command == "h" or command == "home":
                show_timeline(args)
            if command == "stream":
                stream_tweet()
            if command == "p" or command == "post":
                post_tweet(args)
            if command == "r" or command == "retweet":
                retweet(args)
            if command == "s" or command == "search":
                search_tweets(args)
            if command == "m" or command == "mydata":
                show_mydata()
            if command == "q" or command == "e" or command == "exit":
                sys.exit(0)
            if command == "help":
                print(HELP_MESSAGE)
            if command == "c" or command == "clear":
                os.system("clear")

        except CommandError as e:
            print(e.error_message)
        except OtherError as e:
            print(e.error_message)
        except Exception as e:
            print(ERROR_OTHER)
            print(traceback.format_exc())