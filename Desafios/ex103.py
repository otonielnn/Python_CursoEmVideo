"""
    Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.

    O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(nome='', gols=''):
    if (nome.strip() == ''):
        nome = '<desconhecido>'
    if (gols.isnumeric()):
        gols = int(gols)
    else:
        gols = 0
    return print(f'O jogador {nome} marcou {gols} gols no Campeonato.')


# Programa Principal
nome = input('Nome do Jogador: ')
gols = input('Número de Gols: ')
ficha(nome, gols)
