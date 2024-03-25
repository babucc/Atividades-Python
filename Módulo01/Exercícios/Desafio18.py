import math

co = float(input('Digite um número: '))
ca = float(input('Digite Outro número: '))

hi = math.hypot(co, ca)

print(f'Hipotenusa: {hi:.2f}')

#              OU

co = float(input('Digite um número: '))
ca = float(input('Digite um número: '))

h1 = (co**2+ca**2)**(1/2)

print(f'Hipotenusa: {h1:.2f}')