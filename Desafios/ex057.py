"""
    Faça um programa que leia o sexo de uma pessoa, mas só aceite valores 'M' ou 'F'. Caso esteja errado peça a digitação novamente até ter um valor correto.
"""
sexo = input('Sexo [M/F]: ').strip().upper()
i = 1
while (i != 0):
    if (sexo == 'M' or sexo == 'F'):
        print(f'Você selecionou: {sexo}')
        i = 0
    else:
        print('Sexo Inválido.')
        sexo = input('Sexo [M/F]: ').upper()
