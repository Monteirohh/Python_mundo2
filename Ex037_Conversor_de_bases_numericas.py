num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[  1  ] Converter número binário     
[  2  ] Converter número OCTAL
[  3  ] Converter número HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para binário é igual a {}.'.format(num, bin(num) [2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}.'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)))
else:
    print('Opção invalida, tente novamente.')