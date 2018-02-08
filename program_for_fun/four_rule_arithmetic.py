# four_rule_arithmetic.py


def four_rule(choice, a, b):
    if choice == 1:
        result = a + b
    if choice == 2:
        result = a - b
    if choice == 3:
        result = a * b
    if choice == 4:
        result = a / b
    return result


while True:
    c = int(input("""1. +
2. -
3. *
4. /
5. quit
input your choice :"""))
    if c == 5:
        break
    if c not in [1, 2, 3, 4, 5]:
        print("Error")
        break
    a = int(input("first :"))
    b = int(input("second :"))
    print(four_rule(c, a, b))
