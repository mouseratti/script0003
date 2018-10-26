#!/usr/bin/env python

FILENAME = "file1.txt"



class B:

    def __enter__(self):
        print("__enter__ called")

    def __exit__(self, *args):
        print("__exit__ called with args {}".format(args))





if __name__ == '__main__':
    with open(FILENAME, "r+") as f:
        # result = [line for line in f]
        result1 = []
        for line in f.readlines():
            result1.append(line)

    with open(FILENAME, "r+") as f:
        result2 = [line for line in f]

    assert result1 == result2