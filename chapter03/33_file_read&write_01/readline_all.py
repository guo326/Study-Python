# readline_all.py

f = open("C:/Python/exercise/chapter03/33_file_read&write_01/new.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()
