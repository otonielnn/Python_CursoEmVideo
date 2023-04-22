"""
    Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
from time import sleep
from random import randint
lista = list()
jogos = list()
c = 0
print('-' * 30)
print('      JOGA NA MEGA SENA           ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while (total <= quant):
    c = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            c += 1
        if c >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    print(f'Os números sorteados foram: {jogos}')
    total += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 4, '< Boa Sorte! >', '-=' * 5)
