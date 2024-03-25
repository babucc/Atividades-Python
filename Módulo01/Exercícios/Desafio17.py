import math

num = float(input('Digite um número: '))

inteiro = math.trunc(num)

print(f'Numero: {inteiro}')

#              OU

num = float(input('Digite um número: '))

print(f'O número digitado é: {num} e sua parte inteira: {int(num)}')