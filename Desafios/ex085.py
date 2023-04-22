"""
    Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e Ímpares. No final mostre os valores pares e Ímpares em ordem crescente.
"""
lista = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite {i}º valor: '))
    if (n % 2 == 0):
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'O valores Pares digitados foram: {lista[0]}')
print(f'O valores Ímpares digitados foram: {lista[1]}')
