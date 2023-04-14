"""
    Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
maior = 0
menor = 0
print('Análise de Pesos')
for i in range(1, 6):
    peso = float(input(f'Digite o {i}º Peso: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if (peso > maior):
            maior = peso
        else:
            menor = peso

print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
