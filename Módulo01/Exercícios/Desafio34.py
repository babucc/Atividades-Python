sala = float(input("Qual o seu salário?: R$"))

if sala > 1250:
    aumento = sala + (sala * 10/100)
else:
    aumento = sala + (sala * 15/100)

print(f"Novo salário: R${aumento}")