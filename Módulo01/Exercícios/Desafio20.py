import random

alu1 = input('Nome 01: ')
alu2 = input('Nome 02: ')
alu3 = input('Nome 03: ')
alu4 = input('Nome 04: ')

alunos = [alu1, alu2, alu3, alu4]
sorteio = random.choice(alunos)

print(f'Escolhido: {sorteio}')

#             OU

import random

alunos = 'Carlos', 'Danilo','Fael', 'Jurere'
sorteio = random.choice(alunos)

print(f'{sorteio}')