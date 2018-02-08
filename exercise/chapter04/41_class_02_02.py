class Service:
    secret = "귄분은 귀엽다"  # 유용한 정보

    def sum(self, a, b):    # 더하기 정보
        result = a + b
        print("%s + %s = %s입니다" % (a, b, result))


Guin = Service()

print(Guin.sum(1, 1))

print(Service.sum(Guin, 1, 1))
