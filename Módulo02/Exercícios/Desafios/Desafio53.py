frase = input("Digite uma frase: ").lower().strip()

junto = frase.replace(" ", "")
inverso = ""

for f in range(len(junto)-1,-1,-1):
    inverso += junto[f]

if inverso == junto:
    print("Essa frase É um palíndromo!")
else:
    print("Essa frase NÃO é um palíndromo!")