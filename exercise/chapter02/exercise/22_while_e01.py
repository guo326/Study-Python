f = open("C:\Python\exercise\chapter02\exercise\while_new.txt", 'w')
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        f.write(str(money) + " 커피를 줍니다\n")
        coffee = coffee - 1
    elif money > 300:
        f.write((str(money) + " 거스름돈 %d를 주고 커피를 줍니다\n" % (money - 300)))
        coffee = coffee - 1
    else:
        f.write("""돈을 다시 돌려주고 커피를 주지 않습니다
        남은 커피의 양은 %d개 입니다\n""" % coffee)
    if not coffee:
        f.write("커피가 전부 떨어졌습니다 판매를 중지합니다")
        break
f.close()
