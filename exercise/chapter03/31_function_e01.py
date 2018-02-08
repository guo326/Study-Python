def def1(str1, *args):
    if str1 == "커피":
        num = 0
        for i in args:
            num = num + i
    if str1 == "도넛":
        num = 0
        for i in args:
            num = num + i
    return num

print(def1("커피", 1, 2, 3, 4, 5))
