a = 3
print(type(3))
print(type(a))
print(type('b'))
print(type((1, 2, 3)))
print(type([1, 2, 3]))
print(type({1, 2, 3}))
print(type({1: 'hi'}))

a = 3
b = 3
print(a is b)

import sys
print(sys.getrefcount(3))

a = 3
print(sys.getrefcount(3))
b = 3
print(sys.getrefcount(3))
c = 3
print(sys.getrefcount(3))

a, b = ('python', 'hoo')
print(a)
print(b)
print(a, b)
(a, b) = 'python', 'hoo'
print(a)
print(b)
print(a, b)

[a, b] = 'python', 'hoo'
print([a, b])
a = b = 'python'
print(a)
print(b)

a = 3
b = 5
print(a)
print(b)
print(a, b)
a, b = b, a
print(a)
print(b)
print(a, b)

a = 3
b = 3
del(a)
del(b)

a = [1, 2, 3]
b = a
a[1] = 4
print(a)
print(b)

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

from copy import copy
b = copy(a)
print(b is a)
