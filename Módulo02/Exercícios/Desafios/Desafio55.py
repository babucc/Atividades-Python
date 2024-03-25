pesos = []

for i in range(1, 6):
    peso = float(input("Qual o seu peso?: "))
    pesos.append(peso)

maior = max(pesos)
menor = min(pesos)

print(f"Maior peso: {maior}")
print(f"Menor peso: {menor}")