from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta em {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: Mirim.')
elif idade <= 14:
    print ('Classificação: infantil.')
elif idade <= 19:
    print('Classificação: Junior.')
elif idade <=25:
    print('Classificação: Sênior.')
else:
    print('Classificação: MAster.')