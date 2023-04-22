"""
    faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
        - Quantas pessoas foram cadastradas.
        - Uma listagem com as pessoas mais pesadas.
        - Uma listagem com as pessoas mais leves.
"""
pessoas = list()
pessoas1 = list()
pesadas = leves = 0
while True:
    pessoas1.append(str(input('Nome: ')))
    pessoas1.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        pesadas = leves = pessoas1[1]
    else:
        if pessoas1[1] > pesadas:
            pesadas = pessoas1[1]
        if pessoas1[1] < leves:
            leves = pessoas1[1]
    pessoas.append(pessoas1[:])
    pessoas1.clear()
    q = ''
    while (q != 's' and q != 'n'):
        q = input('Deseja continuar [S/N]: ').strip().lower()
    if (q == 'n'):
        break
print(pessoas)
print(f'{len(pessoas)/2:.0f} Foram cadastradas.')
print(f'O Maior peso foi de Kg {pesadas}', end=' ')
for p in pessoas:
    if (p[1] == pesadas):
        print(f'{p[0]}', end=' ')
print(f'\nO Menor peso foi de Kg {leves}', end=' ')
for p in pessoas:
    if (p[1] == leves):
        print(f'{p[0]}', end=' ')
