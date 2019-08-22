# coding: utf-8


import random


def shuf(s):
    length = len(s)
    if length <= 4:
        return s
    middle = list(s[1 : length - 1])
    random.shuffle(middle)
    return s[0] + "".join(middle) + s[length - 1]


if __name__ == "__main__":
    random.seed()
    s = "abcdefghijklmnopqrstuvwxyz"
    print(shuf(s))
