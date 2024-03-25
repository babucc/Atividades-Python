dez = []

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))

for p in range(primeiro,50+1,razão):
    dez.append(p)
print(dez[0:10])