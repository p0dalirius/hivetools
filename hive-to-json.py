#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : hive-to-json.py
# Author             : Podalirius (@podalirius_)
# Date created       : 18 Dec 2021

import argparse
import os
from Registry import Registry
from rich.progress import track
import json


def parseArgs():
    print("%30s -  by Remi GASCOU (Podalirius)\n" % "hive-to-json v1.2")
    parser = argparse.ArgumentParser(description="Description message")
    parser.add_argument("-H", "--hive", default=None, required=True, help='Hive file to convert to json')
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


def get_value_of(key):
    try:
        value = reg.open(key)
        return value
    except Registry.RegistryKeyNotFoundException:
        return None


def dict_setitem_by_path(data, path, value):
    tmp = data
    for key in path[:-1]:
        if key not in tmp.keys():
            tmp[key] = {}
        tmp = tmp[key]
    tmp[path[-1]] = value
    return data


if __name__ == '__main__':
    options = parseArgs()
    data = {}
    if os.path.exists(options.hive):
        reg = Registry.Registry(options.hive)
        list_reg_keys = get_all_keys(reg.root())
        for regkey in track(list_reg_keys, description="Converting hive ..."):
            entries = get_value_of(regkey).values()
            for entry in entries:
                if entry.value_type() == Registry.RegSZ or entry.value_type() == Registry.RegExpandSZ:
                    path = regkey.split('\\') + [entry.name()]
                    dict_setitem_by_path(data, regkey.split('\\'), entry.value())

        if options.outfile is not None:
            basedir = os.path.dirname(options.outfile)
            if not os.path.exists(basedir):
                os.makedirs(basedir)
            f = open(options.outfile, 'w')
            f.write(json.dumps(data, indent=(4 if options.pretty else None)))
            f.close()
        else:
            print(json.dumps(data, indent=(4 if options.pretty else None)))

    else:
        print('[!] File %s does not exist or is not readable.' % options.hive)
