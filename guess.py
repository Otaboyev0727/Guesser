import random
n = random.randint(1,10)
guess= int(input("1 dan 10 gacha son kiriting:"))
guesses = 0
while True:
    if n == guess:
        print("Topdingiz")
        break   
    if guesses >= 3:
        print("Yutqadizngiz")
        break
