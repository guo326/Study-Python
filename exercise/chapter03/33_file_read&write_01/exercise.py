print("f(filename, number) to read your file, if number = 0, it will read all")


def f(name, num):
    f = open(name, 'r')
    line = f.read(num)
    if num == 0:
        line = f.read()
        f.close()
        return line
    f.close()
    return line


if __name__ == "__main__":
    print(f("new.txt", 15))
    print(f("new.txt", 30))
    print(f("new.txt", 0))
    print(type(f("new.txt", 0)))
