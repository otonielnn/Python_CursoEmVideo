"""
    Estrutura de repetição For
"""
inicio = int(input('início: '))
final = int(input('Fim: '))
passo = int(input('passo: '))

for i in range(inicio, final+1, passo):
    print(i)
print('Fim')
