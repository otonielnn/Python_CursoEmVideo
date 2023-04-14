"""
    Faça um programa que leia um número inteiro e diga se ele é ou não primo. (nnúmero divisivel por 1 e ele  mesmo apenas.)
"""
print('Número primo')
n = int(input('Digite um número: '))
c = 0
for i in range(1, n+1):
    if (n % i == 0):
        print('\033[33m', end=' ')
        c += 1
    else:
        print('\033[31m', end=' ')
    print(f'{i}', end=' ')
print(f'\n\033[mO número foi divisível {c} vezes')
if (c == 2):
    print(f'\33[32mO número {n} É Primo!!!')
else:
    print(f'\33[31mO número {n} NÃO É Primo!!!')
