"""
   Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    - O primeiro valor é maior
    - O segundo valor é maior
    - não existe valor maior, os dois são iguais. 
"""
print('Seja bem-vindo ao comparador de números')
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

if (n1 > n2):
    print(f'O número {n1} é o maior')
elif (n1 < n2):
    print(f'O número {n2} é o maior')
else:
    print('Não existe um número maior. Os dois são iguais')
