primeiro = int(input('primeiro termo: '))
razao = int(input('Razão: '))
décimo = primeiro + (10 -1) * razao
for c in range(primeiro, décimo, razao):
    print('{}'.format(c), end='-  ')
print('ACABOU')

