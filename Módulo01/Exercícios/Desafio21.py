import random

alunos = ['Danilo', 'Carlos', 'Fael', 'Jurere']

random.shuffle(alunos)

print(f'Ordem de apresentação: {alunos}')

#              OU

import random

alu1 = input('Digite seu nome: ')
alu2 = input('Digite seu nome: ')
alu3 = input('Digite seu nome: ')
alu4 = input('Digite seu nome: ')

alunos = [alu1, alu2, alu3, alu4]

random.shuffle(alunos)

print(f'Ordem: {alunos}')