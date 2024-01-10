#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics for web server logs.
"""

import sys

total_file_size = 0
status_count = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
processed_lines = 0

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            initial_processed_lines = processed_lines
            if tokens[-2] in status_count:
                status_count[tokens[-2]] += 1
                processed_lines += 1
            try:
                total_file_size += int(tokens[-1])
                if initial_processed_lines == processed_lines:
                    processed_lines += 1
            except FileNotFoundError:
                if initial_processed_lines == processed_lines:
                    continue
        if processed_lines % 10 == 0:
            print("Total File Size: {:d}".format(total_file_size))
            for key, value in sorted(status_count.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("Total File Size: {:d}".format(total_file_size))
    for key, value in sorted(status_count.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("Total File Size: {:d}".format(total_file_size))
    for key, value in sorted(status_count.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
