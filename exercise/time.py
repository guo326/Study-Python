import datetime
t = datetime.datetime.now()
print(t)


import time
now = time.localtime()
a = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
print(a)


b = "%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
print(b)

print(type(now.tm_sec))
print(now.tm_sec)

for i in range(11):
    i = i + 1
    print(i)
    time.sleep(10)


while True:
    import time
    now = time.localtime()
    print(now.tm_sec)
    if now.tm_sec == 30:
        print("정분입니다")
        break
