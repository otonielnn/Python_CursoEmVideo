"""
    Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não antingiram a maior idade e quantas já são maiores.

    Considere maior idade 21 anos
"""
import datetime
print('Análise de Idades')
maior = 0
menor = 0
ano = datetime.date.today().year
for i in range(1, 8):
    nascimento = int(input(f'Em qual ano nasceu a {i}º Pessoa: '))
    idade = ano - nascimento
    if (idade >= 21):
        maior += 1
    else:
        menor += 1

print(f'Temos {maior} maiores de idade, e {menor} menores de idade')
