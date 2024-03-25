soma = 0
idade_mais_velho = 0
homem_mais_velho = ""
total20 = 0

for p in range (1,5):
    print(f"-------- PESSOA 0{p} -------- ")
    nome = input("Informe o seu nome: ").upper()
    idade = int(input("Informe a sua idade: "))
    sexo = input("Qual é o seu gênero? [M/F]: ").lower().strip()

    soma += idade
    media = soma/4

    if p == 1 and sexo == "m":
        idade_mais_velho = idade
        homem_mais_velho = nome
    if sexo == "m" and idade > idade_mais_velho:
        idade_mais_velho = idade
        homem_mais_velho = nome
    if sexo == "f" and idade < 20:
        total20 += 1

print(f"A média de idade do grupo é: {media} anos.")
print(f"O homem mais velho é: {homem_mais_velho} com {idade_mais_velho} anos.")
print(f"Quantidade de mulheres com menos de 20 anos é de {total20}")