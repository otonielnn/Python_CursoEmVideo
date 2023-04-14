"""
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final mostre:
        - A média de idade do grupo
        - Qual é o nome do homem mais velho
        - quantas mulheres tem menos de 20 anos.
"""
print('Análise de pessoas')
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
mulher20 = 0
for i in range(1, 5):
    nome = input(f'Digite o nome da {i}º pessoa: ').strip()
    idade = int(input(f'Digite a idade da {i} pessoa: '))
    sexo = input('Sexo [M/F]: ').lower()
    somaIdade += idade
    if (i == 1 and sexo == 'm'):
        maiorIdadeHomem = idade
        nomeVelho = nome
    if (sexo == 'm' and idade > maiorIdadeHomem):
        maiorIdadeHomem = idade
        nomeVelho = nome
    if (sexo == 'f' and idade < 20):
        mulher20 += 1


mediaIdade = somaIdade/4
print(f'A Média de idade do grupo é {mediaIdade}.')
print(f'O homem mais velho tem {maiorIdadeHomem} e se chama {nomeVelho}.')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos.')
