# coding: utf-8

def element_pos_dic(s):
    element_names = [x.rstrip(",") for x in s.split(" ")]
    word_indices = dict()
    for i in range(len(element_names)):
        # 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
        if i == 0 or 4 <= i <= 8 or 15 <= i <= 16 or i == 19:
            word_indices[element_names[i][0]] = i + 1
        else:
            word_indices[element_names[i][0:2]] = i + 1

    return word_indices


if __name__ == "__main__":
  s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
  print(element_pos_dic(s))
