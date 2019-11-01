#!/usr/bin/env python3
import bz2,os
w=b''
for x in bz2.open(__file__[:-5]+'c').read().split(b'%'):
 if x:w=w[:len(w)-x[0]]+x[1:]
 else:w+=b"'s"
 print(w.decode())
