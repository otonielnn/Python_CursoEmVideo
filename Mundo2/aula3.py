"""
    Estrutura de Repetição While
"""
i = 1
par = 0
impar = 0
while i != 0:
    i = int(input('Digite um valor: '))
    if (i != 0):
        if (i % 2 == 0):
            par += 1
        else:
            impar += 1
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
print('fim')
