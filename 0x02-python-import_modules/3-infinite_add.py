#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    infinite_add = 0
    for i in range(1, len(sys.argv)):
        infinite_add += int(sys.argv[i])
    print("{}".format(infinite_add))
