f = open("C:\Python\exercise\chapter02\exercise/new.txt", 'w')

a = 0

while True:
    a = a + 1
    if a < 10:
        data = "%d번째 완\n" % a
        f.write(data)
    else:
        data = "완\n"
        f.write(data)
        break

for i in range(1, 11):
    if i < 10:
        data = "%d번째 완\n" % i
        f.write(data)
    else:
        data = "완\n"
        f.write(data)
f.close()

