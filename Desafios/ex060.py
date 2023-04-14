"""
    Faça um programa que leia um número qualquer e mostre o seu fatorial.
    5! = 5x4x3x2x1 = 120
"""
print('Calculo Fatorial')
n = int(input('Digite um número: '))
c = n
f = 1
while (c > 0):
    f *= c
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(f)
