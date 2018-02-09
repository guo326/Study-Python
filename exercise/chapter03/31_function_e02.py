class SM:
    def __init__(self, name):
        self.name = name

    def sum(self, *args):
        a = 0
        for i in args:
            a = a + i
        print("%s님 sum 계산 결과는" % self.name)
        return a

    def mul(self, *args):
        a = 1
        for i in args:
            a = a * i
        print("%s님 mul 계산 결과는" % self.name)
        return a


guin = SM("GB")
print(guin.sum(1, 2, 3, 4, 5))
print(guin.mul(1, 2, 3, 4, 5, 6, 7))
