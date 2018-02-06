# writedata.py

f = open("C:/Python/exercise/chapter03/33_file_read&write_01/new.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다\n" % i
    f.write(data)
f.close()
