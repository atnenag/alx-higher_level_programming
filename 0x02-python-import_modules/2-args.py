#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_arguments = len(argv)
    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("1 argument:")
    else:
        print(f"{num_arguments} arguments:")
    if num_arguments == 0:
        print(".")
    else:
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
