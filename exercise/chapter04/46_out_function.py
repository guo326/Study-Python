import pickle
f = open("test.txt", 'wb')
data = {1: "a", 2: "b"}
pickle.dump(data, f)
f.close()

f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
f.close()

import os
print(os.environ)
print(os.environ['PATH'])
print(os.getcwd())
print(os.system("dir"))

import shutil
shutil.copy("test.txt", "new.txt")

import time
print(time.time())
print(time.localtime())
print(time.asctime())
print(time.ctime())

import calendar
print(calendar.calendar(2017))
print(calendar.prmonth(2017, 12))

import random
print(random.random())
print(random.randint(1, 10))

import webbrowser
webbrowser.open_new_tab("http:/naver.com/")
