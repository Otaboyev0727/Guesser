import random
guess= int(input("1 dan 10 gacha son kiriting:"))
n= random.randint(1, 10)
if n==guess:
    print("Topdingiz")
else:
    print("Topa olmadingiz")
