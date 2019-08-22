# coding: utf-8


def cat_chars_by_turn(s1, s2):
    result = ""
    for i in range(len(s1) + len(s2)):
        idx = int(i / 2)
        if i % 2 == 0:
            result += s1[idx]
        else:
            result += s2[idx]

    return result


if __name__ == "__main__":
    s1, s2 = "パトカー", "タクシー"
    print(cat_chars_by_turn(s1, s2))
