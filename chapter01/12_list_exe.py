# list exercise

odd = [1, 3, 5, 7, 9]

a = "Life is too short"
b = a.split()
print(b)

# list indexing

a = [1, 2, 3]
print(a)
print(a[0])
print(b[0])
print(a[0] + a[2])
print(a[0] + a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3][0])

a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])

# list slicing

a = [1, 2, 3, 4, 5]
print(a[0:2])

a = [1, 2, ["a", "b", "c"], 3]
print(a[:3])
print(a[2][:2])
print(a[1:4])

# list +-*/

a = [1, 2, 3]
b = [3, 4, 5]
print(a+b)
print((a+b)[1:5])
print(a*3)
print((a*3)[2])

a = [1, 2, 3]
print(str(a[2])+"hi")

# list modification

a = [1, 2, 3]
print(a)
a[2] = 4
print(a)
print(a[1:2])
a[1:2] = ['a', 'b', 'c']
print(a)

a = [1, 2, 4]
a[1] = ['a', 'b', 'c']
print(a)

a = [1, 2, 3]
print(a)
a[2] = 4
print(a)
a[1:2] = ['a', 'b', 'c']
print(a)
a[1:3] = []
print(a)
a[1:2] = ['b', 'c']
print(a)
a[1] = ['!', '@', '#']
print(a)
a[1][1] = ['abc', 'ABC', 0x12, 0o12]
print(a)
print(a[1][1][1])
print(str(a[0]) + "HUHUHU")
del a[1][1][1:3]
print(a)
del a[1]
print(a)

# list function

a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6])
print(a)
a.append('a')
print(a)

a = [1, 13, 63465, 12, 23, 7]
a.sort()
print(a)
a = ["banana", "card", "apple"]
a.sort()
print(a)

a = [5, 6, 1, 8, 3, 9, 12]
a.reverse()
print(a)
a.append(7)
print(a)
a.sort()
print(a)
a.reverse()
print(a)

a = [1, 2, 3]
print(a.index(3))
a = "12345"
print(a.index("3"))

a = [1, 2, 3]
a.insert(2, 5)
print(a)
a = "1"
print(a.join("65432"))
print(a)

a = "12345"
print(a.replace("123", "3"))
print(a)
a = "12345"
print(a.split("3"))

a = [1, 2, 3, 4, 5]
a.insert(2, 7)
print(a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

a = [1, 2, 3]
print(a.pop())
print(a)
a = [1, 2, 3, 1, 2, 3]
print(a.pop(1))
print(a)

a = [1, 2, 3, 1]
print(a.count(1))

a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7]
a.extend(b)
print(a)
