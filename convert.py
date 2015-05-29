#!/usr/bin/python3
import os
from changes import *


BOT_DIR = "bot_sources"
DEFAULT_BOT = "ualberta"


def get_source_files(bot_name):
    source_files = []

    for root, dirs, files in os.walk("./bot_sources/" + bot_name):
        for f in files:
            if f.endswith(".cpp"):
                source_files.append(os.path.join(root, f))

    return source_files


def convert(source):
    return source


if __name__ == "__main__":
    bot = DEFAULT_BOT
    #bot = input("Bot to convert: ")

    files = get_source_files(DEFAULT_BOT)

    for filename in files[:2]:
        old = None
        with open(filename, 'r') as fp:
            old_file = fp.read()
        new = convert(old)
        print(new)
