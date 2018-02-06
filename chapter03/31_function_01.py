# 파이썬 함수의 구조
"""
def 함수명(입력 인수):
    <수행할 문장1>
    <수행할 문장2>
"""


def sum(a, b):
    return a + b


a = 3
b = 4
c = sum(a, b)
print(c)

# 입력값과 결과값에 따른 함수의 형태
"""
일반적인 함수
def 함수이름(입력인수)
    <수행할 문장>
    ...
    return 결과값
"""


def add(c, d):
    result = c + d
    return result


print(add(a, b))

# 입력값이 없는 함수


def say():
    return "hi"


a = say()
print(a)

# 결과값이 없는 함수


def sss(a, b):
    print("%d, %d의 합은 %d입니다" % (a, b, a+b))


print(sss(3, 4))
a = sss(3, 4)
print(a)

# 입력값도 결과값도 없는 함수


def aaa():
    print("hi")


print(aaa())
