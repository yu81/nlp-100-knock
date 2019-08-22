# coding: utf-8

import sys

argc = len(sys.argv)
tail_len = 20
if argc >= 2:
    tail_len_candidate = sys.argv[1]  # str
    if tail_len_candidate.isdigit() and int(tail_len_candidate) > 0:
        tail_len = int(tail_len_candidate)

with open("hightemp.txt", "r") as file:
    lines = file.read().rstrip().split("\n")
    l = len(lines)
    print("\n".join(lines[l - tail_len :]))
