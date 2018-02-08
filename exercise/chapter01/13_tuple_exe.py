# tuple

t01 = ()
t02 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
print(t3)

# tuple indexing

t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[2])

# tuple slicing

print(t1[1:3])
print(t1[:3])
print(t1[3:])

# tuple +*

t2 = (3, 4)
print(t1 + t2)
print(t2*3)

print(t2.count(3))