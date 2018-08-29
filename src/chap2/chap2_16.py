# coding: utf-8

import sys

argc = len(sys.argv)
split_cnt = 4
if argc >= 2:
    split_cnt_candidate = sys.argv[1]  # str
    if split_cnt_candidate.isdigit() and int(split_cnt_candidate) > 0:
        split_cnt = int(split_cnt_candidate)

with open("hightemp.txt", "r") as file:
    lines = file.read().rstrip().split("\n")
    l = len(lines)
    line_per_file = int(l / split_cnt) + 1

    for i in range(split_cnt):
        out_name = "hightemp_split_%d_of_%d.txt" % (i + 1, split_cnt)
        begin = line_per_file * i
        end = line_per_file * (i + 1)
        file_lines = lines[begin:end]
        with open(out_name, "w") as target:
            target.write("\n".join(file_lines))
