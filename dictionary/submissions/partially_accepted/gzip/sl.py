#!/usr/bin/env python3
import gzip,sys
sys.stdout.buffer.write(gzip.open(__file__[:-3]).read())
