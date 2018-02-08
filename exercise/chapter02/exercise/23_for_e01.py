l1 = [1, 2, 3, 4, 5]
for i in l1:
    i = i + 1
    print(i, end=" ")

l2 = [a*b//c for a in range(1, 3)
      for b in range(5, 9)
      for c in range(3, 9)]
print("\n", l2)
s1 = set(l2)
print(s1)
print(l2.count(3))

l3 = [5, 6, 1, 2, 7]
a = 0
b = 0
for i in l3:
    if i > 5:
        a = a + 1
    else:
        b = b + 1
print("햅격 : %s, 불햅격 : %s" % (a, b))

a = 0
b = 0
c = 0
while a < 5:
    if l3[a] > 5:
        b = b + 1
    else:
        c = c + 1
    a = a + 1
print([b, c])
