casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantps anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salário * 30 / 100 
print ('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('A prestão será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print ('Empréstimo pode ser CONCEDIDO')
else: 
    print ('Empréstimo NEGADO!')
    