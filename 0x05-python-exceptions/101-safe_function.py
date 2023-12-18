#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        f = fct(*args)
        return f
    except Exception:
        import sys
        print("Exception: {}".format(Exception), file=sys.stderr)
        return None
