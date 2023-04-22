"""
    Crie um programa que vai gerar cinco números aleatorios e colocar em uma tupla.
    
    Depois disso, mostre a listagem de número gerados e também indique o menor e o maior valor que estão na tupla.
"""
import random
tupla = (random.randint(0, 10), random.randint(0, 10), random.randint(
    0, 10), random.randint(0, 10), random.randint(0, 10))
ordenada = sorted(tupla)
print('Os números sorteados em ordem crescente foram: ', end='')
for i in ordenada:
    print(i, end=' ')
print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
