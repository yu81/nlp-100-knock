# coding: utf-8

def cipher(s):
    code_point = ord(s)
    if ord("a") <= code_point <= ord("z"):
        return chr(219 - code_point)
    return s


if __name__ == "__main__":
    s = "I love NLP and ML."
    result = ""
    for i in range(len(s)):
        result += cipher(s[i])
    print(result)
