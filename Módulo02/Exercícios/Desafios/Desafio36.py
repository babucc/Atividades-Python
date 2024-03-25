valor = float(input("Qual o valor da casa?: "))
salário = float(input("Qual o seu salário?: "))
anos = int(input("Em quantos anos você irá pagar?: "))

num_parcelas = anos * 12
prestação = valor/num_parcelas

limite = 0.3 * salário

if prestação <= limite:
    print("Empréstimo aprovado!")
    print(f"Valor da sua prestação em {anos} anos é de R${prestação:.2f}.")
else: 
    print("Empréstimo negado!")
    print(f"A sua prestação mensal de R${prestação:.2f} excede os 30% do seu salário.")