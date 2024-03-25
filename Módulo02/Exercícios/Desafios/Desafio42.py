r1 = float(input("Reta 01: "))
r2 = float(input("Reta 02: "))
r3 = float(input("Reta 03: "))

# Pode ou não pode formar um triângulo.
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("PODEM formar um trinângulo!")
else:
    print("NÃO PODEM formar um triângulo!")

# Tipo do triângulo.
if r1 == r2 == r3:
    print("Triângulo Equilátero!")
elif r1 != r2 and r1 != r3 and r2 != r3:
    print("Triângulo Escaleno!")
else:
    print("Triângulo Isósceles")