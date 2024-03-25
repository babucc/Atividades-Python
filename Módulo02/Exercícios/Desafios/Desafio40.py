n1 = float(input("Informe a nota 01: "))
n2 = float(input("Informe a nota 02: "))

media = (n1+n2)/2

if media < 5:
    print("REPROVADO!")
elif media >= 5 and media <= 6.9:
    print("RECUPERAÇÃO!")
else:
    print(f"APROVADO com {media}.")