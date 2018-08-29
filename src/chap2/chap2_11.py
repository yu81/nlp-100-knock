# coding: utf-8

with open("hightemp.txt", "r") as file:
    print("".join([line.replace("\t", " ") for line in file]))
