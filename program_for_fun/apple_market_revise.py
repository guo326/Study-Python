# apple_market_revise.py

for apple in range(1, 11):
    money = int(input("pay money for an apple; $10 :"))
    if money == 10:
        print("here is your apple, %d apple(s) remain" % (10 - apple))
    elif money > 10:
        print("you pay a lot, here is your apple and $%d, %d apple(s) remain" % ((money - 10), (10 - apple)))
    else:
        pass
    if apple == 10:
        print("sold out")
