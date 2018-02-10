# random_pop.py

import random
import time


def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)


i = 0
if __name__ == "__main__":
    data = list(range(45))
    while i < 7:
        i = i + 1
        print(random_pop(data))
        time.sleep(1)
