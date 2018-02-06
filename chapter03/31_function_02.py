# 여러 개의 입력값을 받는 함수
"""
def 함수이름(*입력변수):
    <수행할 문장>
    ...
"""


def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


result = sum_many(1, 2, 3)
print(result)

result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)


def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


result = sum_mul('sum', 1, 2, 3, 4, 5)
print(result)
result = sum_mul('mul', 1, 2, 3, 4, 5)
print(result)

# 함수의 결과값은 언제나 하나이다


def sum_and_mul(a, b):
    return a+b, a*b


result = sum_and_mul(3, 4)
print(result)
sum, mul = sum_and_mul(3, 4)
print(sum, mul)
print(sum)

# return의 또 다른 스임새


def say_nick(nick):
    if nick == "바보":
        return
    print("내 별명은 %s야" % nick)


print(say_nick("야호"))
print(say_nick("바보"))
