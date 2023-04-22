"""
    Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre
        - Quantas vezes apareceu o valor 9
        - Em que posição foi digitado o primeiro valor 3.
        - Quais foram os números pares.
"""
v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))
v3 = int(input('Digite o 3º valor: '))
v4 = int(input('Digite o 4º valor: '))

tupla = (v1, v2, v3, v4)
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(tupla.index(3)+1)
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Números pares:')
for i in range(0, 4):
    if (tupla[i] % 2 == 0):
        print(tupla[i])
