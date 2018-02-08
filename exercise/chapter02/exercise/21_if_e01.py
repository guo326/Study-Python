b = ["도끼", "왕왕이", "시바"]
if "도끼" in b:
    print("도끼")
elif "왕왕이" in b:
    print("왕왕이")
else:
    print(b)

for i in b:
    if i == "도끼":
        print("도끼")
    elif i == "왕왕이":
        print("왕왕이")

a = [x*y for x in range(2, 30)
     for y in range(1, 10)]
print(a)

f = open("new_01.txt", 'w')

for x in range(2, 30):
    for y in range(1, 10):
        f.write(str(x*y) + " ")
    f.write('\n')
f.close()
