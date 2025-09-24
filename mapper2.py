#!/usr/bin/env python3
import sys, re
from spellchecker import SpellChecker

spell = SpellChecker()

for line in sys.stdin:
    # normalize curly apostrophes
    line = line.replace("’", "'").lower()
    # match words with any internal apostrophes except leading/trailing
    words = re.findall(r"\b[a-zA-Z]+(?:'[a-zA-Z]+)*\b", line)
    for w in words:
        if w not in spell:
            print(f"{w}\t1")

