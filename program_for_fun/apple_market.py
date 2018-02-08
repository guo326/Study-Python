# apple_market.py

apple = 10
while 1:
    money = int(input("price of an apple is $10, give me money :"))
    if money == 10:
        apple = apple - 1
        print("here is your apple, %d apple(s) remain" % apple)
    elif money > 10:
        apple = apple - 1
        print("you pay a lot, so you take $%d and here is your apple\n%d apple(s) remain" % ((money - 10), apple))
    else:
        print("you need more money to buy an apple")
    if not apple:
        print("no apple, so close market")
        break
