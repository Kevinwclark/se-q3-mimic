#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Kevin Clark with help from Joseph Hafed and JT"


import random
import sys


"""Returns a dict mapping each word to a list of words which follow it.
For example:
    Input: "I am a software developer, and I don't care who knows"
    Output:
        {
            "" : ["I"],
            "I" : ["am", "don't"],
            "am": ["a"],
            "a": ["software"],
            "software" : ["developer,"],
            "developer," : ["and"],
            "and" : ["I"],
            "don't" : ["care"],
            "care" : ["who"],
            "who" : ["knows"]
        }
"""


def create_mimic_dict(filename):
    dictionary = {}
    with open(filename) as f:
        x = f.read()
        lst = x.split()
        last_word = ''
        for word in lst:
            if last_word in dictionary:
                dictionary[last_word].append(word)
            else:
                dictionary[last_word] = [word]
            last_word = word
    return dictionary


def print_mimic_random(mimic_dict, num_words):
    start_word = ''
    for _ in range(num_words + 1):
        print(start_word, end=' ')
        next_word = mimic_dict.get(start_word, mimic_dict[''])
        start_word = random.choice(next_word)

    # start_word = ''
    # for _ in range(num_words):
    #     print(f"{start_word} ")
    #     next_word = mimic_dict.get(start_word)
    #     if start_word in mimic_dict:
    #         start_word = random.choice(next_word)
    #     else:
    #         start_word = random.choice(mimic_dict[''])


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
