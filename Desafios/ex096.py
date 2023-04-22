"""
    Faça um programa que tenha uma função chamada Área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""


def area():
    print('     Controle de Terrenos        ')
    print('-' * 30)
    l = float(input('LAGURA (m): '))
    c = float(input('COMPRIMENTO (m): '))
    return print(f'A área de um terreno {l}x{c} é de {l*c}m².')


area()
