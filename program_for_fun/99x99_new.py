f = open("99x99_new.txt", 'w')

a = [i*j for i in range(100)
     for j in range(100)]
f.write(str(a))

f.close()
