# coding: utf-8


from chap1_05 import ngram

if __name__ == "__main__":
    s1 = "paraparaparadise"
    s2 = "paragraph"
    # union, intersect, diff
    x = ngram(s1, 2)
    y = ngram(s2, 2)
    print(x)
    print(y)

    union = set(x).union(y)
    print(union)

    intersect = set(x).intersection(y)
    print(intersect)

    diff = set(x).difference(y)
    print(diff)

    if "se" in x:
        print('x contains "se"')
    if "se" in y:
        print('y contains "se"')
