# coding: utf-8

def length_of_words(s):
    return [len(x.rstrip(",")) for x in s.split(" ")]


if __name__ == "__main__":
    s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    length_list = length_of_words(s)
    print(length_list)
