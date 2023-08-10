#!/usr/bin/python3
def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return s
    letters = ""
    for number in range(len(s)):
        if number != n:
            letters += s[number]
    return letters
