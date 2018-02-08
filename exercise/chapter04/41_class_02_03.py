class Service:
    secret = "귄분은 귀엽다"  # 유용한 정보

    def setname(self, name):
        self.name = name

    def sum(self, a, b):    # 더하기 정보
        result = a + b
        print("%s님 %s + %s = %s입니다" % (self.name, a, b, result))


Guin = Service()
Guin.setname("귄분이")
print(Guin.sum(1, 1))
