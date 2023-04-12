"""
    Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
import math
print('Seja bem-vindo ao programa maior e menor')
n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))

if (n1 > n2) and (n1 > n3):
    maior = n1
elif (n2 > n1) and (n2 > n3):
    maior = n2
else:
    maior = n3

if (n1 < n2) and (n1 < n3):
    menor = n1
elif (n2 < n1) and (n2 < n3):
    menor = n2
else:
    menor = n3

print(f'O menor número que você digitou, foi: {menor}')
print(f'O maior número que você digitou, foi: {maior}')
