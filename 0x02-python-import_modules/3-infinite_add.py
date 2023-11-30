#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    total = 0
    if count == 0:
        print("0")
    else:
        for i in range(1, count + 1):
            total += int(sys.argv[i])
        print("{}".format(total))
