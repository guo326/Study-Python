# for 문과 continue

marks = [90, 25, 67, 45, 80]
number = 0

for i in marks:
    number = number + 1
    if i > 60:
        print("%d번째 학생 햅격 축하" % number)
    else:
        continue

number = 0

for i in marks:
    number = number + 1
    if i < 60:
        continue
    print("%d번째 학생 햅격 축하" % number)
