# readline.py

f = open("C:/Python/exercise/chapter03/33_file_read&write_01/new.txt", 'r')
line = f.readline()
print(line)

print(f.readline(5))

f.close()


class A:
    def __init__(self, num):
        f = open("new.txt", 'r')
        self.line = f.readline(num)


guin = A(10)
print(guin.line)

f = open("new.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()