"""
   Crie um programa que faça o computador jogar jokenpô com você. 
"""
import random
import time
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''Suas opções:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura''')
jogador = int(input('Digite a sua opção: '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)
print(f'O computador escolheu {itens[computador]}')
print(f'Você escolheu {itens[jogador]}')

if (computador == 0):
    if (jogador == 0):
        print('A partida ficou EMPATADA')
    elif (jogador == 1):
        print('O JOGADOR VENCEU')
    elif (jogador == 2):
        print('O COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif (computador == 1):
    if (jogador == 0):
        print('O COMPUTADOR VENCEU')
    elif (jogador == 1):
        print('A partida ficou EMPATADA')
    elif (jogador == 2):
        print('O JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif (computador == 2):
    if (jogador == 0):
        print('O JOGADOR VENCEU')
    elif (jogador == 1):
        print('O COMPUTADOR VENCEU')
    elif (jogador == 2):
        print('A partida ficou EMPATADA')
    else:
        print('JOGADA INVÁLIDA')
# print(f'O computador esolheu {itens[computador]}')
