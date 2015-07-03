#!/usr/bin/python3
from __future__ import print_function
import os
from sys import argv
from changes import simple_replace, warn_issues, manual_fix
import re

# Python 2/3 compatibility
try:
    input = raw_input
except NameError:
    pass


def _yesno(message, default='no', suffix=' '):
    """Modified from github.com/tylerdave/prompter to reduce depenencies.
    All credit to the creator."""
    if default == 'yes':
        yesno_prompt = '[Y/n]'
    elif default == 'no':
        yesno_prompt = '[y/N]'
    else:
        raise ValueError("default must be 'yes' or 'no'.")

    if message != '':
        prompt_text = "{0} {1}{2}".format(message, yesno_prompt, suffix)
    else:
        prompt_text = "{0}{1}".format(yesno_prompt, suffix)

    while True:
        response = input(prompt_text).strip()
        if response == '':
            return True
        else:
            if re.match('^(y)(es)?$', response, re.IGNORECASE):
                if default == 'yes':
                    return True
                else:
                    return False
            elif re.match('^(n)(o)?$', response, re.IGNORECASE):
                if default == 'no':
                    return True
                else:
                    return False


def get_source_files(path):
    """Given a path name, grab all .cpp files in that directory, recursively."""
    source_files = []

    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(".cpp"):
                source_files.append(os.path.join(root, f))

    return source_files


def convert(source):
    """Convert a source string from BWAPI version 3 to 4."""
    modified = simple_replace(source)
    return modified


def save_converted_files(files, old_root, new_root):
    """Save files from old_root into new_root."""
    if os.path.exists(new_root) and\
       _yesno("Warning: output directory already exists. Continue?"):
        exit(0)
        print("Not writing files into existing directory. Quitting.")

    bot_directories = []
    new_files_and_paths = []
    for old_path, new_file in files:
        rel_path = os.path.relpath(old_path, old_root)
        new_path = os.path.join(new_root, rel_path)
        new_dir = os.path.dirname(new_path)  # May not be a new directory.
        print("{} \t-> \t{}".format(old_path, new_path))

        bot_directories.append(new_dir)
        new_files_and_paths.append((new_path, new_file))

    for directory in bot_directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

    for path, source in new_files_and_paths:
        with open(path, 'w') as fp:
            fp.write(source)


if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: python3 convert.py path/to/old_bot/ path/to/new_bot/")
        exit(-1)

    old_root = argv[1]
    new_root = argv[2]

    files = get_source_files(old_root)
    converted_files = []

    for filename in files:
        old = None
        with open(filename, 'r') as fp:
            old = fp.read()
        new = convert(old)
        converted_files.append((filename, new))

    save_converted_files(converted_files, old_root, new_root)
