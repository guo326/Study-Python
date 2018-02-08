num = 0

while 1:
    input()
    num = num + 1
    if num <= 15:
        print("safe")
    elif num <= 19:
        print("warning")
    if num == 20:
        print("stop")
        break
