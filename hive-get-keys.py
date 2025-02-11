#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : hive-get-keys.py
# Author             : Podalirius (@podalirius_)
# Date created       : 18 Dec 2021

import argparse
import os
from Registry import Registry
from rich.progress import track
import json


def parseArgs():
    print("%30s -  by Remi GASCOU (Podalirius)\n" % "hive-get-keys v1.2")
    parser = argparse.ArgumentParser(description="Description message")
    parser.add_argument("-H", "--hive", default=None, required=True, help='Hive file to convert to json')
    parser.add_argument("-k", "--key", default=None, required=True, help='Hive file to convert to json')
    parser.add_argument("-v", "--verbose", default=False, action="store_true", help='arg1 help message')
    return parser.parse_args()


def get_value_of(reg, key):
    try:
        return reg.open(key)
    except Registry.RegistryKeyNotFoundException:
        return None


if __name__ == '__main__':
    options = parseArgs()
    data = {}
    if os.path.exists(options.hive):
        reg = Registry.Registry(options.hive)
        if options.verbose:
            print("[debug] Accessing registry key '%s' ..." % options.key)
        regkey = '\\'.join(options.key.split('\\')[:-1])
        variable = options.key.split('\\')[-1]
        data = get_value_of(reg, regkey)
        if data is not None:
            entries = data.values()
            if len(entries) != 0:
                for entry in entries:
                    if entry.value_type() == Registry.RegSZ or entry.value_type() == Registry.RegExpandSZ:
                        path = regkey.split('\\') + [entry.name()]
                        print("[%s\\%s]: %s" % (regkey, entry.name(), entry.value()))
            else:
                print("[!] Registry key '%s' exists but is empty." % options.key)
        else:
            print("[!] Registry key '%s' does not exist." % options.key)
    else:
        print('[!] File %s does not exist or is not readable.' % options.hive)
