import math

angulo = float(input('Digite um ângulo: '))

se = math.sin(math.radians(angulo))
co = math.cos(math.radians(angulo))
ta = math.tan(math.radians(angulo))

print(f'Seno: {se:.2f}')
print(f'Cosseno: {co:.2f}')
print(f'Tangente: {ta:.2f}')

#              OU

from math import radians, sin, cos, tan

angulo = float(input('Digite um ângulo: '))

se = sin(radians(angulo))
co = cos(radians(angulo))
ta = tan(radians(angulo))

print(f'Seno: {se:.2f}')
print(f'Cosseno: {co:.2f}')
print(f'Tangente: {ta:.2f}')