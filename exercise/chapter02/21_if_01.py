# if

money = 1
if money:
    print("택시를 타고 가세요")
else:
    print("걸어 가세요")

"""
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
"""

x = 3
y = 2
print(x > y)
if x > y:
    print("guin")
else:
    print("nyom")
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)

x = 0
y = 3
if x > y:
    print("to the moon")
else:
    print("what? %d" % x)
    while x <= y:
        x = x + 1
        if x > y:
            print("to the moon")
        else:
            print("what? %d" % x)

money = 2000
if money >= 3000:
    print("택시 고고싱")
else:
    print("걸어서 가요")

money = 2000
card = 1
if money >= 3000 or card:
    print("택시")
else:
    print("걸어")

print(1 in [1, 2, 3])
print(1 not in {1: 'a', 2: 'b'})

print('a' in ('a', 'b', 'c'))
print('k' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시")
else:
    print("걸어")

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("걸어")