#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        s = fct(*args)
        return s
    except Exception as err:
        import sys
        print("Exception: {}".format(err), file=sys.stderr)
        return None
