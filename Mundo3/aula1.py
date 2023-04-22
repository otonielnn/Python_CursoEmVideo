"""
    Tuplas
        - As tuplas são imutáveis
"""

"""
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

for cont in range(0, len(lanche)):
    print(lanche[cont])

for p, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {p}')
print('Comi pra caramba!')
print(sorted(lanche))  # poem em ordem alfabetica/númerica
"""

"""
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(2))
# mostra posição do parametro passado. segundo parametro é a posição de inicio
print(c.index(5, 1))
"""

pessoa = ('Otoniel', 21, 'M', 81.6)
del (pessoa)
print(pessoa)
