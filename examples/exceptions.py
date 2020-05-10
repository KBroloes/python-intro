import os

f = None
try:
    f = open('tempfile', 'r')
    f.read()
except FileNotFoundError as err:
    print(err)
finally:
    if f is not None:
        f.close()