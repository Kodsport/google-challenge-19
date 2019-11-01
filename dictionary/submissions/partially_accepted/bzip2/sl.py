#!/usr/bin/env python3
import bz2,sys
sys.stdout.buffer.write(bz2.open(__file__[:-3]).read())
