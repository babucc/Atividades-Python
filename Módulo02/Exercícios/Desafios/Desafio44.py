preço = float(input("Informe o preço do produto: "))
print("         FORMAS DE PAGAMENTO")
print("1- À vista dinheiro/cheque: 10% de desconto.")
print("2- À vista no cartão: 5% de desconto.")
print("3- Em até 2x no cartão: preço normal.")
print("4- 3x ou mais no cartão: 20% de juros.")
escolha = int(input("Forma de pagamento escolhida: "))

if escolha == 1:
    desconto = preço * 0.1
    print(f"Novo valor: R${preço - desconto}")
elif escolha == 2:
    desconto = preço * 0.05
    print(f"Novo valor: R${preço - desconto}")
elif escolha == 3:
    parcela = preço / 2
    print(f"Será parcelado em 2x de R${parcela}")
    print(f"Valor: R${preço}")
elif escolha == 4:
    parcelas = int(input("Quantas parcelas?: "))
    parcelado = preço / parcelas
    juros = preço * 0.20
    print(f"Será parcelado em {parcelas}x de R${parcelado+(parcelado*0.20)} com JUROS")
    print(f"Novo valor: R${preço + juros}")