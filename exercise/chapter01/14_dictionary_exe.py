# dictionary

dic = {'name': 'guin', 'phone': '01000009052', 'birth': '0710'}
a = {1: 'hi'}
a = {'a': [1, 2, 3]}
print(dic)
print(a)

a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'guin'
print(a)
a[3] = [1, 2, 3]
print(a)
del a[1]
print(a)

# use dictionary

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

a = {1: 'a', 2: 'b'}
print(a[1])
print(a[2])
a = {'a': 1, 'b': 2}
print(a['a'])
print(a['b'])

print(dic['name'])
print(dic['phone'])
print(dic['birth'])

a = {1: 'a', 1: 'b'}
print(a[1])

a = {(1, 2): 'a'}
print(a[(1, 2)])

# dictionary function

a = {'name': 'guin', 'phone': '01000009052', 'birth': '1008'}
print(a.keys())
print(list(a.keys()))
print(a.values())
print(list(a.values()))
print(a.items())
print(list(a.items()))
print(a.clear())
print(a)

a = {'name': 'guin', 'phone': '010000009052', 'birth': '1008'}
print(a.get('name'))
print(a.get('phone'))
print(a.get('nyom'))
print(a.get('foo', 'oh'))
print(a.get('name', 'oh'))
print('name' in a)
print('foo' in a)
