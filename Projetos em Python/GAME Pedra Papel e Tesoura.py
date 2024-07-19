from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if  computador == 0:
     if jogador == 0:
         print('EMPATE')
     elif jogador == 1:
        print('O JOGADOR VENCEU')
     elif jogador == 2:
         print('O COMPUTADOR VENCEU')
     else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
     if jogador == 0:
        print('O COMPUTADOR VENCEU')
     elif jogador == 1:
          print('EMPATE')
     elif jogador == 2:
          print('O JOGADOR VENCEU')
     else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
       print('O JOGADOR VENCEU')
    elif jogador == 1:
         print('O COMPUTADOR VENCEU')
    elif jogador == 2:
         print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')



