#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        s = fct(*args)
        return s
    except Exception:
        import sys
        print("Exception: {}".format(Exception), file=sys.stderr)
        return None
