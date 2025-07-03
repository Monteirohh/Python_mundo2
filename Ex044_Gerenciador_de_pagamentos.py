print('{:=^40}'.format('MONTEIROS'))
preco = float(input('Preço das compras: R$ '))
print('''FORMAR DE PAGAMENTO
[  1  ] a vista dinheiro / cheque
[  2  ] á vista cartão
[  3  ] 2x no cartão     
[  4  ] 3x ou mais no cartão
''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} no final.'.format(preco, total))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(int('Quantas parcelas? '))
    parcela = total / totparc
print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(totparc, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))
