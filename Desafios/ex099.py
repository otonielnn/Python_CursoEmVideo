"""
    Faça um programa que tenha um função maior(), que reebar vários parâmetros com valores inteiros.

    Seu programa tem que analisar todos os valores e dizer qual deles é maior.
"""
from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
        if (cont == 0):
            maior = n
        else:
            if (n > maior):
                maior = n
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

    # Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
