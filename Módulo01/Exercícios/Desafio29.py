vel = int(input("Velocidade: "))

multa = 7
max = 80
km_amais = vel - max

if vel <= 80:
    print("Dentro do limite permitido!")
else:
    print(f"Você foi MULTADO em R${km_amais * multa}!")