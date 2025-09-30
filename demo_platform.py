#! /usr/bin/env python3
# Author: KVijay
# Description: This script will demo
"""
    Docstring:
"""
import sys
import os

my_home = None

if sys.platform == "win32":
    my_home = os.environ['HOMEPATH']
elif sys.platform == "darwin" or sys.platform == "linux":
    my_home = os.environ['HOME']
else:
    print("On some other OS")

print("Home is", my_home)