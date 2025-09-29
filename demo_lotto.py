#! /usr/bin/env python3
# Author: KVijay
# Description: This script will demo
"""
    Docstring:
"""
import random

lotto = []

while len(lotto) < 6:
    num = random.randint(1, 50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate number =", num)


print("lottery numbers =", lotto)