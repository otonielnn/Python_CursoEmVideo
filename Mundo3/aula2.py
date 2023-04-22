"""
    Listas
        - Mútavel
        - lista.append('biscoito') # adiciona item no final da lista
        - lista.insert(0, 'biscoito') # adiciona na posição passada como parametro
        - del lista[3] # remove
        - lista.pop(3) # remove o valor na posição passada como parametro
        - lista.pop() # remove o último item
        - lista.remove('biscoito')
        - valores = list(range(4,11)) # gera lista [4, 5, 6, 7, 8, 9, 10]
        - lista.sort() # deixa lista em ordem
        - lista.sort(reverse=True) # deixa a lista em ordem reversa
"""
"""
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
"""

"""
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
"""
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista b: {b}')
