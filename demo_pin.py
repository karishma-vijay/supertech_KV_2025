#! /usr/bin/env python3
# Author: KVijay
# Description: This script will demo
"""
    Docstring:
"""

master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("valid pin")
        break
    else :
        print("invalid pin")
        attempts += 1

print("Done")