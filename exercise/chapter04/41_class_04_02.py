class HouseGuin:
    lastname = "Guin"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s, %s로 여행을 가다" % (self.fullname, where))


guin = HouseGuin("bun")
print(type(guin))
print(guin.travel("London"))
