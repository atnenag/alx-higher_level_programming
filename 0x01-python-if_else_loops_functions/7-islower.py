#!/usr/bin/env python3
def islower(c):
    lowercase_range = range(ord('a'), ord('z')+1)
    return ord(c) in lowercase_range
