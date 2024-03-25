dias = int(input('Quantos dias rodados?: '))
km = float(input('Quantos KM rodados?: '))

t = (dias*60)+(km*0.15)

print(f'Total a ser pago: R${t:.2f}')