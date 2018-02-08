class HouseGuin:
    lastname = "Guin"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print("%s, %s로 여행을 가다" % (self.fullname, where))

    def __add__(self, other):
        print("%s, %s 결혼하셨어" % (self.fullname, other.fullname))

    def __sub__(self, other):
        print("%s와 %s는 Ryzen2600을 만났어" %(self.fullname, other.fullname))


class HouseRyzen(HouseGuin):
    lastname = "Ryzen"

    def travel(self, where):
        print("%s는 %s로 여행을 가고 싶다" % (self.fullname, where))


guin = HouseGuin("bun")
cpu = HouseRyzen("2400G")
print(guin.travel("London"))
print(cpu.travel("USA"))
print(guin + cpu)
print(guin - cpu)
