# coding: utf-8

import sys

with open("hightemp.txt", "r") as file:
    records = [line.split("\t") for line in file.read().rstrip().split("\n")]
    records.sort(key=lambda x: x[2], reverse=True)
    print("\n".join(["\t".join(line) for line in records]))
