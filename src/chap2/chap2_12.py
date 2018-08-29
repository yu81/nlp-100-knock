# coding: utf-8

text = ""
outfile = "col1.txt"
with open("hightemp.txt", "r") as file:
    text = "\n".join([line.rstrip().split("\t")[0] for line in file])

with open(outfile, "w") as target:
    target.write(text)
