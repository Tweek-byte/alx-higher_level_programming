#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics for web server logs.
"""

import sys

total_size = 0
status_counts = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
line_counter = 0

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            previous_counter = line_counter
            if tokens[-2] in status_counts:
                status_counts[tokens[-2]] += 1
                line_counter += 1
            try:
                total_size += int(tokens[-1])
                if previous_counter == line_counter:
                    line_counter += 1
            except FileNotFoundError:
                if previous_counter == line_counter:
                    continue
        if line_counter % 10 == 0:
            print("Total Size: {:d}".format(total_size))
            for key, value in sorted(status_counts.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("Total Size: {:d}".format(total_size))
    for key, value in sorted(status_counts.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("Total Size: {:d}".format(total_size))
    for key, value in sorted(status_counts.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
