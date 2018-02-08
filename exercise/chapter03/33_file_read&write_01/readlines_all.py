# readlines_all.py

f = open("C:/Python/exercise/chapter03/33_file_read&write_01/new.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
