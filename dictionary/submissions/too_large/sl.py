#!/usr/bin/env python3
import bz2,os
w=b''
for x in bz2.open(__file__[:-3]).read().split(b'%'):
 if x:w=w[:len(w)-x[0]]+x[1:]
 else:w+=b"'s"
 print(w.decode())

"""
                          ::::::
            MMMMMMMMMM    ::::::
          MMMMMMMMMMMMMMMMMM::::
          SSSSSS::::SS::  SSSSSS
        SS::SS::::::SS::::::SSSS
        SS::SSSS::::::SS::::::SS
        SSSS::::::::SSSSSSSSSS
            ::::::::::::::SS
    SSSSSSSSSSMMSSSSSSMMSS
  SSSSSSSSSSSSSSMMSSSSSSMM    SS
::::SSSSSSSSSSSSMMMMMMMMMM    SS
::::::    MMSSMMMMMM::MM::MMSSSS
  ::  SS  MMMMMMMMMMMMMMMMMMSSSS
    SSSSSSMMMMMMMMMMMMMMMMMMSSSS
  SSSSSSMMMMMMMMMMMMMM
  SS    MMMMMMMM
"""
