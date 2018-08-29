# coding: utf-8

import sys

argc = len(sys.argv)
head_len = 20
if argc >= 2:
    head_len_candidate = sys.argv[1]  # str
    if head_len_candidate.isdigit() and int(head_len_candidate) > 0:
        head_len = int(head_len_candidate)

with open("hightemp.txt", "r") as file:
    cnt = 0
    for line in file:
        print(line.rstrip())
        cnt += 1
        if cnt >= head_len:
            break
