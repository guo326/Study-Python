# exercise string 01

#multi line
print("""
여러줄은 큰따옴표 세개로
나타내거나 작은 따옴표 세개로
넘기면 됩니다
""")
multi1 = '''
for multi line
need """or \'\'\'
use to it
'''
print(multi1)

print("이런 방법으로\n줄을 바꿀수도\n있습니다\\")

# string +-*/

a = "abcde"
b = "ABCDE"

print(a + b)
print(a * 3)
print(a.replace("ab", "ac"))

a = "a b c d e"
print(a.split())
print(a.count(a))

print("="*50)
print("{0:^50}" .format("hi"))
print("="*50)

# string index & slicing

c = "Good man, Bad man, Ugly man"
print(c)
print(c[:8])
print(c[8])
print(c[10:17])
print(c[:10] + c[19:])
print(c[8]*5)

d = "20150217Movie"
date = d[:8]
doing = d[8:]
year = d[:4]
day = d[4:8]
print(date)
print(doing)
print(year)
print(day)
print(day + doing)
print(year + day)

e = 3.123141423
print("%0.3f" % e)
print("{0:0.3f}" .format(e))
print("{{date}} is {0}" .format(date))
print("{date} is %s" % date)
print("date is %s, year is %s, day is %s, that day %s, I did %s" % (date, year, day, day, doing))
print(str(215))
f = int(date)
print(f)
print("date is %d" % f)
g = list(year)
h = g + list(day)
print(g)
print(h)
print(h.pop())
print(h)
i = h + list(doing)
print(i)
print(h.sort())

if date == "1201":
    print("nop")
elif "Movie" in doing:
    print("go to movie")
else:
    while f < 30000000:
        f = f * 2
        print(str(f))

C = {c: "movie"}
print(list(c))
print(tuple(c))
print(c)
print(dict(C))

k = {0: a, 1: b, 2: c, 3: d}
print(k[0])

L = 0
l = []
while L < 100:
    L = L + 1
    if L % 2 == 0:
        continue
    l.append(L)
print(l)
del l[:25]
print(l)
