"""
    Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
        - Qual é o tatal gasto na compra.
        - Quantos produtos custam mais de R$1000.
        - qual é o nome do produto mais barato.
"""
mais1000 = total = menor = c = 0
barato = ''
while (True):
    nome = input('Digite o nome do produto: ').strip()
    preço = float(input('Digite o preço do item R$: '))
    c += 1
    resp = ''
    total += preço
    if (c == 1 or preço < menor):
        menor = preço
        barato = nome
    if (preço > 1000):
        mais1000 += 1
    while (resp != 's' and resp != 'n'):
        resp = input('Quer continuar [S/N]: ')
    if (resp == 'n'):
        break
print(f'O total da comprar foi R${total:.2f}')
print(f'temos {mais1000} Produtos a cima de R$1000')
print(f'{barato} foi o item mais barato. que custá: {menor:.2f}')
