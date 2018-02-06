# for
"""
for 변수 in 리스트(or 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
"""

# 전형적인 for문

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 다양한 for문의 사용

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print("a =", first)
    print("b =", last)
    print("a + b =", first + last)

(f, l) = (1, 2)
print(f)
print(l)
print(f, l)
