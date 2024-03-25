nome = input('Dige o nome da sua cidade: ').strip().lower()

inicio = nome.split()

print("Santo" in inicio[0:5]) # (:5) Limita o nome a 4 caracteres.