class HouseGuin:
    lastname = "Guin"

    def setname(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s, %s로 여행을 가다" % (self.fullname, where))


guin = HouseGuin()
print(type(guin))
print(guin.lastname)
guin.setname("bun")
print(guin.fullname)
print(guin.travel("London"))

