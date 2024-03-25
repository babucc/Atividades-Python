from datetime import date

ano = int(input("Informe o seu ano de nascimento: "))

ano_atual = date.today().year  
idade = ano_atual - ano

if idade < 18:
    saldo = 18 - idade
    print(f"Você ainda irá se alistar, daqui a {saldo} anos!")
elif idade == 18:
    print("Está na hora de se alistar!")
else:
    saldo = idade - 18
    print(f"Passou do prazo de se alistar a {saldo} anos!")
  