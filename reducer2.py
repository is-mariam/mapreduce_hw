#!/usr/bin/env python3
import sys
from collections import defaultdict

counts = defaultdict(int)
for line in sys.stdin:
    word, n = line.strip().split('\t')
    counts[word] += int(n)

for word, total in counts.items():
    print(f"{word}\t{total}")

