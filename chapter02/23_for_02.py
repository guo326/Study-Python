# for문의 응용

marks = [90, 25, 67, 45, 80]
number = 0
for i in marks:
    number = number + 1
    if i > 60:
        print("%s번째 학생 햅격" % number)
    else:
        print("%s번째 학생 불햅격" % number)
