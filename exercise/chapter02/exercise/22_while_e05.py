a = 0
b = 0
while a < 50 and b < 10:
    a = a + 1
    b = b + 0.2
    c = a * b
    print("%0.3f" % c)
    if c > 100:
        break
