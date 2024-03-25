num = int(input("Informe um número: "))
print("Escolha a base de conversão:")
print("1- Binário")
print("2- Octal")
print("3- Hexadecimal")
base = int(input("Sua opção: "))

if base == 1:
    resultado = bin(num)
    print(f"O número {num} em binário é: {resultado[2:]}")
elif base == 2:
    resultado = oct(num)
    print(f"O número {num} em octal é: {resultado[2:]}")
elif base == 3:
    resultado = hex(num)
    print(f"O número {num} em hexadecimal é: {resultado [2:]}")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")