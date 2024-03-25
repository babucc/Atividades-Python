from datetime import date

ano = int(input("Informe o seu ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano

if idade <= 9:
    print(f"{idade}: Mirim")
elif idade > 9 and idade <= 14:
    print(f"{idade}: Infantil")
elif idade > 14 and idade <= 19:
    print(f"{idade}: Junior")
elif idade > 19 and idade <= 20:
    print(f"{idade}: Sênior") 
else:
    print(f"{idade}: Master")