# exercise for string

multiline = "Life is too short\nYou need Python\n"
print(multiline)
multiline = """Life is
tooooo \tshort\\
You need Python"""
print(multiline)

head = "\npython"
tail = " nyomnyoom"
print(head + tail)
print(head*5)
print("="*50)
print('hello')
print("="*50)
a = ("f", "cf", "gr")
b = ("a", "f", "ad")
print(a + b)

# index & slice

a = "Life is too short, You need Python"
print(a[3])
print(a[3]*5+a[1:15])
print(a[3:-1]*3+a[5:7]*3)

b = 3
if b < 5:
    print(a[3:9])

a = "20180204Nyomm"
date = a[:8]
weather = a[8:]
print(date)
print(weather)
print(a)
year = a[:4]
day = a[4:8]
print("\n"+year)
print(day)
print(weather)
print(a)
a = "20150123WOWOWOW"
date = a[:8]
feel = a[8:]
print(date)
print(feel)

a = "pithon"
print(a[1])
print(a[0]+"y"+a[2:])

# string formatting

print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 3
print("I eat %d apples" % number)
number = 10
day = "three"
print("I ate %d apples. so I was nyom for %s days." % (number, day))
number2 = 15
print("I ate %d apples and %o grapes" % (number, number2))
print("I ate %s apples, so I was nyom for %s days. And ate %s grapes" % (number, day, number2))
print("\nError is %d%%." % 98)

print("%15s" % "hi")
print("%-10s\\\njane" % "hi")
print("%150s" % "hi")
print("%-15sjane" % "hi")

print("%0.4f" % 3.42134234)
print("%0.4f" % 3.1231412553)
print("%10s%0.4f" % ("", 3.42134234))
print("%10.4f" % 3.42134234)
print("%10.5f" % 3.12391283)

a = "hobby"
print(a.count('b'))
a = "neeeeeeeeeewewewewewewwwweee"
print(a.count('e'))
a = "python is best choice"
print(a)
print(a.find('b'))
print(a.find('k'))
a = "Life is too short"
print(a)
print(a.index('t'))
a = ","
print(a.join('abcd'))
a = "hi"
b = "nyom"
print(a.upper())
print(b.upper())
a = "Hi"
print(a.lower())
a = " 'hi'"
print(a.lstrip())
a = "'hi' "
print(a.rstrip())
a = " hi "
print(a.strip())
a = "Life is too short"
print(a.replace("Life", "Your leg"))
a = "Life is too short"
print(a.split())
a = "a:b:c:d"
print(a.split(":"))

print("%0.4f" % 3.1235123)
print("%0.8s" % 3.1234123)