# coding: utf-8

def template_07(x, y, z):
    return "%d時の%sは%.1f" % (x, y, z)


if __name__ == "__main__":
    x = 12
    y = "気温"
    z = 22.4
    print(template_07(x, y, z))
