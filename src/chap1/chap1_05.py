# coding: utf-8


def ngram(s, n):
    result = list()
    if type(s) == str or type(s) == list:
        for i in range(len(s) - n + 1):
            result.append(s[i : i + n])
    return result


if __name__ == "__main__":
    s = "I am an NLPer"
    print(ngram(s, 2))
    print(ngram(s.split(" "), 2))
