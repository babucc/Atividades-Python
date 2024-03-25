r1 = float(input("Reta 01: "))
r2 = float(input("Reta 02: "))
r3 = float(input("Reta 03: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("PODEM formar um trinângulo!")
else:
    print("NÃO PODEM formar um triângulo!")