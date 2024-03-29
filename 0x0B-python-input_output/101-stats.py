#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics for web server logs.
"""


def print_statistics(total_size, status_codes):
    """
    Print file size and status code statistics.
    """
    print("File size: {}".format(total_size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_codes = {}
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_statistics(total_size, status_codes)
                line_count = 1
            else:
                line_count += 1

            line = line.split()

            try:
                total_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise
