num = int(input("Digite um número: "))

total = 0

for n in range(1, num+1):
    if num % n == 0:
        total += 1

if total == 2:
    print(f"{num} É um número primo!")
else:
    print(f"{num} NÃO é um número primo")