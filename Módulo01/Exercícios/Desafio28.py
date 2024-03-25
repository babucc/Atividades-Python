import random

alea = random.randint(0, 5)

acho = int(input("Em qual número estou pensando?: "))
if acho == alea:
    print("Você acertou!")
else:
    print(f"GANHEI! Eu pensei no {alea} e não no {acho}!")
    