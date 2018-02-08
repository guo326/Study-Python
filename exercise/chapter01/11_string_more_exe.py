# expert string formatting exercise hard

print("I eat %d apples" % 3)
print("I eat %s apples" % 3)
print("I eat {0} apples".format(3))

print("I eat %s apples" % "five")
print("I eat {0} apples".format("five"))

number = 10.129501239
day = "three"
print("I ate %d apples. so I was nyom for %s days" % (number, day))
print("I ate %s apples. so I was nyom for %s days" % (number, day))
print("I ate %0.3f apples. so I was nyom for %s days" % (number, day))
print("I ate {0} apples. so I was nyom for {1} days".format(number, day))
print("I ate {number} apples. so I was nyom for {day} days" .format(number=10, day="three"))
print("I ate {0} apples. so I was nyom for {day} days" .format(10, day="three"))

print("%10s" % "hi")
print("%-10s" % "hi")
print("{0:<10}" .format("hi"))
print("{0:>10}" .format("hi"))
print("%5s%5s" % ("hi", ""))
print("{0:^10}" .format("hi"))
print("{0:=^10}" .format("hi"))
print("{0:!<10}" .format("hi"))
print("{0:>10}" .format("hi"))
print("="*50 + "\n")
print("{0:^50}" .format("hmm"))
print("\n" + "="*50)

y = 3.1383823712
print("%0.4f" % y)
print("{0:0.4f}" .format(y))
print("I ate {0} apples. And I ate {1:0.4f} grapes. so I was nyom for {2} days" .format(number, y, day))
print("{0:10.4f}" .format(y))
print("{0:^10.4f}" .format(y))
print("{{guinbun}}huhu" .format())
