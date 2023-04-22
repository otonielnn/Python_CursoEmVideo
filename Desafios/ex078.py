"""
    Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
    
    No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = list()
for i in range(0, 5):
    valor = int(input(f'Digite um valor para a Posição {i}: '))
    lista.append(valor)
print('=-' * 30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for i, n in enumerate(lista):
    if n == max(lista):
        print(f'{i}... ', end='')
print(f'\nO maior valor digitado foi {min(lista)} nas posições ', end='')
for i, n in enumerate(lista):
    if n == min(lista):
        print(f'{i}... ', end='')
