n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais número: "))

maior = n1
menor = n1

# Maior
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")


#           OU

'''n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais número: "))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print(f"O maior é: {maior}")
print(f"O menor é: {menor}")'''
