nome = input('Digite o seu nome completo: ')

# Mostra todas as letras em Maiúsculas.
print(nome.upper())
# Mostra todas as letras em Minúsculas.
print(nome.lower())
# Substitui os espaços presentes na frase por "", assim, juntando a frase.
sem = nome.replace(" ", "")
# Mostra a quantidade de caracteres depois de substituir.
print(len(sem))
# Mostra letras tem o primeiro nome.
dividido = nome.split()
primeiro = dividido[0]
print(len(primeiro))