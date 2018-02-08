# calculator class


class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

    def minus(self, num):
        self.result -= num
        return self.result

    def multi(self, num):
        self.result *= num
        return self.result

    def divis(self, num):
        self.result /= num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))
print(cal2.minus(5))
print(cal2.multi(5))
print(cal2.divis(5))
