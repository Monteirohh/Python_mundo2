n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0 

while opção != 5:

    print('''[ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')

    opção = str(input('Qual é a sua opção? R: '))

    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('A soma entre {} + {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('A soma entre {} + {}'.format(n1, n2, maior))
    elif opção == 4:
        print(' Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5: 
        print('Finalizado...')
    else:
        print('Opção inválida. Tente novamente.')
        print('=-=' * 10)
        sleep(2)

print('Fim do programa! Volte sempre!')
