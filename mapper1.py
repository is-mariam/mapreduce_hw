#!/usr/bin/env python3
import sys, re

for line in sys.stdin:
    for word in line.strip().split():
        # Remove all punctuation except - _ '
        word = re.sub(r"[^\w\-_']", "", word)  # \w = a-zA-Z0-9
        word = word.lower()
        if word:
            print(f"{word}\t1")

