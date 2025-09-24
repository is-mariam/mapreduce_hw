#!/usr/bin/env python3
import sys
from collections import defaultdict

counts = defaultdict(int)
for line in sys.stdin:
    try:
        word, n = line.strip().split('\t')
        counts[word] += int(n)
    except:
        continue

for word, total in sorted(counts.items()):
    print(f"{word}\t{total}")
