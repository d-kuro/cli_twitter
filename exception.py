#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from error_message import *

class CommandError(Exception):
    def __init__(self):
        self.__error_message = ERROR_COMMAND

    @property
    def error_message(self):
        return self.__error_message

class OptionError(Exception):
    def __init__(self):
        self.__error_message = ERROR_OPTIONS

    @property
    def error_message(self):
        return self.__error_message

class OtherError(Exception):
    def __init__(self):
        self.__error_message = ERROR_OTHER

    @property
    def error_message(self):
        return self.__error_message