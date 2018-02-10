print(abs(-3))
print(all([1, 2, 3]))
print(any([0, 3, 6]))
print(chr(5))
print(dir([1, 2, 3]))
print(divmod(2, 3))
for i, name in enumerate([1, 2, 3]):
    print(i, name)
print(eval("'a' + 'hi'"))

def positive(x):
    return x > 0
print(list(filter(positive, [-1, 0, -3, 1, 5])))

print(hex(159))
a = 3
print(id(a))
print(id(3))

print(int("3"))
print(int(3.1231284))

class Person: pass
a = Person()
print(isinstance(a, Person))

sum = lambda a, b: a + b
print(sum(3, 4))

print(len("ajlkefjaslejflkasjefklsjakldjfej;f"))
print(list("asklfjklesajefkljekl"))

def two_times(x): return x*2
print(list(map(two_times, [1, 2, 3, 4, 5])))

print(max([1, 2, 3]))
print(min("dcaeb"))
print(oct(142))
print(ord('a'))
print(pow(3, 2))
print(list(range(1, 100, 5)))
print(sorted([8, 5, 1, 6, 7, 3]))
