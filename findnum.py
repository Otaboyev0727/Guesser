import math
import random


def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f" Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end=" ")
    while True:
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Kattaroq son ayting: ", end="")
        elif taxmin > tasodifiy_son:
            print("Kichikroq son ayting:", end="")
        else:
            print("YUTDINGIZ!!!")
            break


sontop()
