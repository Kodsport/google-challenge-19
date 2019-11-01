#!/usr/bin/env pypy

from __future__ import print_function
import sys
import random

def cmdlinearg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default

random.seed(int(cmdlinearg('seed', sys.argv[-1])))
n = int(cmdlinearg('n'))
m = int(cmdlinearg('m'))
print(n, m)
li = [random.randint(1, 10) for _ in range(n)]
print(*li)
