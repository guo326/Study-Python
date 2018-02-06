# break while

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다")
    coffee = coffee - 1
    print("커피가 %d개 남았습니다" % coffee)
    if not coffee:
        print("커피 다 떨어졌습니다 판매를 중지합니다")
        break
