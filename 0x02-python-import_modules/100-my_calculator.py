#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a, op, b = map(int, sys.argv[1:4])
    operator = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print(f"{a} {op} {b} = {operator[op](a, b)}")
