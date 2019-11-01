import sys

img = sys.stdin.read()

# JPG magic bytes
assert img[0:3] == "\xFF\xD8\xFF"

sys.exit(42)
