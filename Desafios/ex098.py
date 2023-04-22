"""
    Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo realize a contagem.
    
    seu programa tem que realizar três contagens atravês da função criada:
        A) de 1 até 10, de 1 em 1
        B) de 10 até 0, de 2 em 2
        C) uma contagem personalizada
"""
from time import sleep


def contador():
    print('-=' * 30)
    print('Contagem de 1 até 10 de 1 em 1: ')
    sleep(2)
    for i in range(1, 11):
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
    print('Fim!')
    print('Contagem de 10 até 0 de 2 em 2: ')
    sleep(2)
    for i in range(10, -1, -2):
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
    print('Fim!')
    i = int(input('Inicio: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))

    if (p < 0):
        p *= -1
    if (p == 0):
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')

    if (i < f):
        cont = i
        while (cont <= f):
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!!!')
    else:
        cont = i
        while (cont >= f):
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim!!!')


contador()
