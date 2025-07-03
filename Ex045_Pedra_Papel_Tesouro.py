from random import randint
itens = ('Pedra' , 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções 
   [  0  ] Pedra
   [  1  ] Papel
   [  2  ] Tesoura''')

jogador = int(input('Qual é sua jogada? '))

print('-=' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('JOgador jogou {}'.format(itens[jogador]))

if computador == 0: # Computador jogou Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence.')
    elif jogador == 2:
        print('Computador vence.')
    else:
        print('JOGADA INVÁLIDA!')
if computador == 1: #Computador jogou Papel.
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #Computador jogou tesoura.
    if jogador == 0: 
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('JOGADA INVÁLIDA!')