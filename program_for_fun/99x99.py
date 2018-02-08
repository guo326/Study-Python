f = open("99x99.txt", 'w')

for i in range(100):
    for j in range(100):
        a = i*j
        f.write("%4s " % a)
    f.write("\n")

f.close()
