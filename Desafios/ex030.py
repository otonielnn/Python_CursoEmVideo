"""
    Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.
"""
print('Seja bem-vindo ao impar ou par')
n = int(input('Digite um número: '))
if (n % 2 == 0):
    print(f'O número {n} é Par')
else:
    print(f'O número {n} é Impar')
