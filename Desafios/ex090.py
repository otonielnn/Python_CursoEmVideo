"""
    Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.
"""
aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))

print('-=' * 20)
if (aluno['media'] >= 7):
    aluno['situacao'] = 'Aprovado'
elif (5 <= aluno['media'] < 7):
    aluno['situacao'] = 'em Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print('-=' * 20)
print(f'O {aluno["nome"]} com Média {aluno["media"]} está {aluno["situacao"]}.')
print('-=' * 20)
