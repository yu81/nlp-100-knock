# coding: utf-8

def pick_odd_chars(s):
    return s[::2]


if __name__ == "__main__":
    s = "パタトクカシーー"
    print(pick_odd_chars(s))
