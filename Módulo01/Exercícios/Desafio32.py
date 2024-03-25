from datetime import date

ano = int(input("Qual ano você quer analisar?: "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f"{ano} é Bissexto")
else:
    print(f"{ano} não é Bissexto")