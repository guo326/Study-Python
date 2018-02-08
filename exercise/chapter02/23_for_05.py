# 리스트 안에 for문 포함하기 => 리스트 내포

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

a = [1, 2, 3, 4]
result = [num*3 for num in a]
print(result)
r1 = result[:]
result = [num*3 for num in a if num % 2 == 0]
print(result)
print(r1)
result = [num*3 for num in a if not num % 2 == 0]
print(result)

# 리스트 내포의 일반적인 문법 : [표현식 for 항목 in 반복가능개체 if 조건]
"""
좀더 복잡하게
[표현식 for 항목 in 반복가능개체 if 조건
    for 항목 in 반복가능개체 if 조건
    ...]
"""

result = [x*y for x in range(2, 10)
          for y in range(1, 10)]
print(result)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
r3 = [n1*3+n2 for n1 in a if n1 < 3
      for n2 in b if n2 > 8]
print(r3)
