s = 0 
cont = 0

for i in range(1,7):
    num = int(input("Escreva um número: "))
    if num % 2 == 0:
        s += num
        cont += 1
print(f"Soma de {cont} números pares: {s}")