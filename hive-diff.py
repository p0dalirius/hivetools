#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : hive-diff.py
# Author             : Podalirius (@podalirius_)
# Date created       : 26 Nov 2021

import argparse
import os
from Registry import Registry
from rich.progress import track
import json


def parseArgs():
    print("%30s -  by @podalirius_\n" % "hive-diff v1.2")
    parser = argparse.ArgumentParser(description="Description message")
    parser.add_argument("-A", "--hive-a", default=None, required=True, help='Hive file to convert to json')
    parser.add_argument("-B", "--hive-b", default=None, required=True, help='Hive file to convert to json')
    parser.add_argument("-o", "--outfile", default=None, help='arg1 help message')
    parser.add_argument("-v", "--verbose", default=False, action="store_true", help='arg1 help message')
    parser.add_argument("-p", "--pretty", default=False, action="store_true", help='arg1 help message')
    return parser.parse_args()


def get_all_keys(key, found_keys=[], depth=0):
    if len(key.subkeys()) == 0:
        found_keys.append(key.path().split('ROOT\\', 1)[1])
    else:
        for subkey in key.subkeys():
            found_keys = get_all_keys(subkey, found_keys=found_keys, depth=(depth+1))
    return found_keys

if __name__ == '__main__':
    options = parseArgs()
