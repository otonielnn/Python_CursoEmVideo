"""
    Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
print("Progressão aritmética v2.0")
primeiro = int(input('Digite o Termo Inicial: '))
razao = int(input('Digite a Razão: '))
termo = primeiro
cont = 1

while (cont <= 10):
    print(f'{termo}')
    termo += razao
    cont += 1
print('Fim')
