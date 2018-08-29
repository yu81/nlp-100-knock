# coding: utf-8

import sys

with open("hightemp.txt", "r") as file:
    lines = file.read().rstrip().split("\n")
    chars = [list(line.rstrip().split("\t")[0]) for line in lines]
    print(set(zip(*chars)))
