class Service:
    secret = "귄분은 귀엽다"

    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다" % (self.name, a, b, result))


Guin = Service("귄분이")
print(Guin.sum(1, 1))
