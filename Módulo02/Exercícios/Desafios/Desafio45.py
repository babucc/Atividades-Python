import random

opções = ["pedra", "papel", "tesoura"]

escolha_pc = random.choice(opções)

escolha_eu = input("Pedra, papel ou tesoura?: ").lower()

if escolha_pc == escolha_eu:
    print(f"Empatamos! Também escolhi {escolha_pc}.")
elif (escolha_pc == "pedra" and escolha_eu == "tesoura") or \
    (escolha_pc == "papel" and escolha_eu == "pedra") or \
    (escolha_pc == "tesoura" and escolha_eu == "papel"):
    print(f"Venci! Escolhi {escolha_pc}.")
else:
    print(f"Você venceu! Eu escolhi {escolha_pc}.")