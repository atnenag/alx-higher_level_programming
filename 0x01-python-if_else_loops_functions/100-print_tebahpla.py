#!/usr/bin/python3
for alphabet in range(122, 96, -1):
    ASCII_alphabet = chr(alphabet)
    if alphabet % 2 == 0:
        ASCII_alphabet = ASCII_alphabet.lower()
    else:
        ASCII_alphabet = ASCII_alphabet.upper()
    print(f"{ASCII_alphabet}", end="")
