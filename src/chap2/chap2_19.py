# coding: utf-8

import sys

with open("hightemp.txt", "r") as file:
    lines = file.read().rstrip().split("\n")
    chars = [c for c in [list(line.rstrip().split("\t")[0]) for line in lines]]
    counter = dict()
    for x in chars:
        for y in x:
            if y not in counter:
                counter[y] = 1
            else:
                counter[y] += 1
    result = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    print("\n".join(["\t".join([kv[0], str(kv[1])]) for kv in result]))
