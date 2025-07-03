from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {}.'.format(nasc,idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente.')
elif idade < 18:
    saldo = 19 - idade
    print('Ainda faltam {} anos para o alistamente'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format())
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    