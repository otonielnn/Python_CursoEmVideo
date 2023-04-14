"""
    Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues:

    obs: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
"""
valor = int(input('Digite o valor do saque R$: '))
total = valor
cedula = 50
cedulas = 0
while (True):
    if (total >= cedula):
        total -= cedula
        cedulas += 1
    else:
        if (cedulas > 0):
            print(f'Total de {cedulas} de {cedula}')
        if (cedula == 50):
            cedula = 20
        elif (cedula == 20):
            cedula = 10
        elif (cedula == 10):
            cedula = 1
        cedulas = 0
        if (total == 0):
            print('Fim')
            break
