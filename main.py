#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# constantMessage
from constant import *
# SIGINTシグナルハンドラ用
import signal
import sys
# 独自コンソール
from console import *
import os

# Ctrl-Cハンドラ
def handler(signal, frame):
        print("##### Ended #####")
        show_console(False)
signal.signal(signal.SIGINT, handler)

# コンソール表示
def show_console(first=True):
    os.system("clear")
    twitter_console = TwitterConsole()
    screen_name = get_my_screen_name()
    sys.ps1 = screen_name
    sys.ps2 = "------>> "

    if first:
        twitter_console.interact(HELLO_MESSAGE)
    else:
        twitter_console.interact("")

if __name__ == '__main__':
    show_console()