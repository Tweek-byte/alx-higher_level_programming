#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
"""

import sys
from collections import defaultdict

file_size = 0
status_tally = defaultdict(int)

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            status_code = tokens[-2]

            if status_code in status_tally:
                status_tally[status_code] += 1

            try:
                file_size += int(tokens[-1])
            except ValueError:
                continue

        if i % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(status_tally.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
            i += 1

    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
