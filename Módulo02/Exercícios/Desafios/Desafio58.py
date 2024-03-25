import random

alea = random.randint(0, 10)
cont = 0

acho = int(input("Em qual número estou pensando?: "))
    
while acho != alea:
    if acho != alea:
        cont += 1
    print("Errou, tente novamente!")
    acho = int(input("Em qual número estou pensando?: "))
    
print("Você venceu!")
print(f"Foi necessário {cont+1} palpites para acertar!")