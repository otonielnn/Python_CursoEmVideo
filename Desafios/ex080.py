"""
    Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort).

    no final, mostre a lista ordenada na tela.
"""
lista = list()
for i in range(0, 5):
    n = int(input('Digite um número: '))
    if (i == 0 or n > lista[-1]):
        lista.append(n)
        print('Adicionado na lista...')
    else:
        c = 0
        while (c < len(lista)):
            if (n <= lista[c]):
                lista.insert(c, n)
                print(f'Adicionando na posição {c} da lista...')
                break
            c += 1
print('=-' * 30)
print(f'O valores digitados foram: {lista}')
print('=-' * 30)
