"""
    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
    Para salários superiores a R$1.250,00, calcule um aumento de 10%.
    para Salários inferiores ou iguais, o aumento sera de 15%.
"""
print('Seja Bem-vindo ao calculador de aumento')
salario = float(input('Digite o seu salário: '))
if (salario <= 1250):
    print(
        f'O seu salário de {salario}, com o aumento de 15% ficará {salario + (salario * 0.15):.2f}')
else:
    print(
        f'O seu salário de {salario}, com o aumento de 10% ficará {salario + (salario * 0.10):.2f}')
