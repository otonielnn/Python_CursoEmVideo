"""
    Aprimore o desafio anterior, mostrando no final
        - A soma de todos os valores pares digitados.
        - A soma dos valores terceira coluna.
        - O maior valor da segunda linha.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
somaTerceiraColuna = 0
maiorSegundaLinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {[l, c]}: '))
        if (matriz[l][c] % 2 == 0):
            somaPares += matriz[l][c]

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end=' ')
    print()
print('-=' * 30)
print(f'A soma de Todos valores Pares foi: {somaPares}')
for l in range(0, 3):
    somaTerceiraColuna += matriz[l][2]
print(f'A soma de todos valores da 3º coluna foi: {somaTerceiraColuna}')
for i in range(0, 3):
    if (i == 0 or matriz[1][i] > maiorSegundaLinha):
        maiorSegundaLinha = matriz[1][i]
print(f'O Maior valor da Segunda linha é: {maiorSegundaLinha}')
