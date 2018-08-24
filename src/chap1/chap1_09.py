# coding: utf-8

import random


def shuf(s):
    l = len(s)
    if l <= 4:
        return s
    middle = list(s[1:l - 1])
    random.shuffle(middle)
    return s[0] + "".join(middle) + s[l - 1]


if __name__ == "__main__":
    random.seed()
    s = "abcdefghijklmnopqrstuvwxyz"
    print(shuf(s))
