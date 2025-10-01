#! /usr/bin/env python3
# Author: KVijay
# Description: This script will demo
"""
    Docstring:
"""
def search_word(pattern= "done", file="/Users/kvt757/SuperTech/SuperTech/PythonExercises/words"):
    lines_matched = 0
    with (open(file, mode="rt") as fh_in):
        for (line_num, line) in enumerate(fh_in, start=1):
            if line.isascii() and pattern in line:
                print(line_num, line, end="")
                lines_matched += 1
    return None

# search_word("done", "/Users/kvt757/SuperTech/SuperTech/PythonExercises/words")
print("-" * 50)
# search_word("banana", "/Users/kvt757/SuperTech/SuperTech/PythonExercises/words" )
search_word()

total_lines= 0
total_lines += search_word("done", "/Users/kvt757/SuperTech/SuperTech/PythonExercises/words")
print (f"total lines matched = {total_lines}")