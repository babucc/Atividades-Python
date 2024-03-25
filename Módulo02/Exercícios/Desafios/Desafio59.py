n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))

alt = 0

while alt != 5:
    print("----- MENU -----")
    print("1- Somar")
    print("2- Multiplicar")
    print("3- Maior")
    print("4- Novos números")
    print("5- Sair")
    alt = int(input("Escolha uma das opções: "))
    
    if alt == 1:
        print(f"Resultado da soma: {n1+n2}")
    if alt == 2:
        print(f"Resultado da multiplicação: {n1*n2}")
    if alt == 3:
        if n1 == n2:
            print(f"Os números são iguais: {n1}")
        if n1 > n2:
            print(f"Maior número: {n1}")
        if n2 > n1:
            print(f"Maior número: {n2}") 
    if alt == 4:
        n1 = float(input("Digite um valor: "))
        n2 = float(input("Digite outro valor: "))
print("Fim do Sistema!")