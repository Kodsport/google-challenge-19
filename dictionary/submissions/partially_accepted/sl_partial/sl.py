#!/usr/bin/env python3
import bz2,os
w=b''
c=0
for x in bz2.open(__file__[:-3]).read().split(b'%'):
 if x:w=w[:len(w)-x[0]]+x[1:]
 else:w+=b"'s"
 print(w.decode())
 c+=1
 if c>40000:
  break
