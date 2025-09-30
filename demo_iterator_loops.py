#! /usr/bin/env python3
# Author: KVijay
# Description: This script will demo
"""
    Docstring:
"""
import sys
heroes = ['JFK', 'ozzy osborne', 'diana', 'pele', 'malcolm x']

for name in heroes:
    print (name, end="\n")

idx = 0

for name in heroes:
    print(name, end="\n")
    heroes[idx] = name.upper()
    idx += 1
print("Heroes =", heroes)

for (idx, name) in enumerate(heroes, start=0):
    print(name, end="\n")
    heroes[idx] = name.upper()
    idx += 1
print("Heroes =", heroes)

for (idx, name) in enumerate(heroes, start=0):
    print(name, end="\n")
    heroes[idx] = name.title()
    idx += 1
print("Heroes =", heroes)

try:
    sys.exit(0)
except SystemExit:
    print("bye babes")

