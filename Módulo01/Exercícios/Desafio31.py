km = int(input("Qual a distância da sua viagem?: "))

if km > 200:
    print(f"Preço da passagem: R${0.45 * km}")
else:
    print(f"Preço da passagem: R${0.50 * km}")
