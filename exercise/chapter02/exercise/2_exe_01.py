money = 2000
health = 10
print("I have %d for my computer and %d health for work" % (money, health))
if money >= 10000:
    print("You can buy a computer")
else:
    print("You must work")
    while money < 10000:
        money = money + 500
        print("You make %d" % money)
        health = health - 1
        print("Your health is %d" % health)
        if money >= 10000:
            print("Finally you can buy a computer")
        if health == 0:
            print("Oh You don't make money for your computer")
            break
while True:
    health = int(input("fill up the health: "))
    if not health <= 0:
        print("I have tiger force go work")
        while money < 10000:
            money = money + 300
            print("You make 300 now {0} money" .format(money))
            health = health - 1
            print("Your health is %d" % health)
            if health == 0:
                print("You don't make money")
                break
            if money >= 10000:
                print("Finally!!")
            else:
                print("must work!")
    break
