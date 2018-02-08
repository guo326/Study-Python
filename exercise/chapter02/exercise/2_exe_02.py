a = 0
while a < 100:
    a = a + 1
    if a % 3 == 0:
        continue
    if a % 5 == 0:
        continue
    if a % 2 == 0:
        continue
    if a % 7 == 0:
        continue
    print(a)
