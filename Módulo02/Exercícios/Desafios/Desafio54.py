from datetime import date

maior = 0
menor = 0

for i in range(0, 7):
    ano = int(input("Informe o seu ano de nascimento: "))
    ano_atual = date.today().year

    idade = ano_atual - ano

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f"{maior}: São maiores de idade.")
print(f"{menor}: São menores de idade.")