# 입력 인수에 초깃값 미리 설정하기


def say_myself(name, old, man=True):
    print("내 이름은 %s입니다" % name)
    print("내 나이는 %s입니다" % old)
    if man is True:
        print("난 남자")
    else:
        print("난 여자")


print(say_myself("귄분", 300))
print(say_myself("귄분", 300, True))
print(say_myself("귄순", 300, False))

# 함수 안에서 선언된 변수의 효력 범위

a = 1


def vartest(a):
    a = a + 1
    return a


print(vartest(a))
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는 방법

a = 1


def vartest1(a):
    while a < 10:
        a = a + 1
    return a


a = vartest1(a)
print(a)


a = 1


def vartest2():
    global a
    a = a + 1


vartest2()
print(a)
