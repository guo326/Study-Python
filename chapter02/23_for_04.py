# for와 함께 자주 사용하는 range 함수

# range 함수

a = range(10)
print(a)
b = range(5, 50)
print(b)

# range 함수의 예시 살펴보기

sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번째 학생 햅격 축하" % (number + 1))

# for와 range를 이용한 구구단

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')
