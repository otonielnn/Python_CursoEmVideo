"""
    Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
"""
from random import randint
from time import sleep

numeros = list()


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(1, 6):
        n = randint(0, 9)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar():
    soma = 0
    for c in numeros:
        if (c % 2 == 0):
            soma += c
    print(f'A soma dos valores PARES da lista é igual a {soma}')


sorteia(numeros)
somaPar()
